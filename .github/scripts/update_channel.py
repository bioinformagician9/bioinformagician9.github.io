#!/usr/bin/env python3
"""Refresh data/channel.js with the channel's latest YouTube numbers.

Runs daily from .github/workflows/update-channel.yml. Standard library only.

- With the YOUTUBE_API_KEY secret: subscribers, total views, video count,
  view counts for every video and details of videos uploaded after the
  site's snapshot (YouTube Data API v3).
- Without it: view counts and titles of the 15 newest videos from the
  channel's public RSS feed. The headline numbers are kept as they were.

Never fails the workflow because YouTube is unreachable: it keeps the
previous data and exits 0.
"""
import json, os, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone

CHANNEL_ID = "UCnXs-Nq1dzMZQOKUHKW3rdw"           # youtube.com/@Bioinformagician
SNAPSHOT = "2026-11-13T00:00:00Z"                   # videos in index.html are up to this date
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "channel.js")
PREFIX = "window.CHANNEL="
API = "https://www.googleapis.com/youtube/v3/"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "bioinformagician-site-updater"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def api(path, key, **params):
    params["key"] = key
    return json.loads(get(API + path + "?" + urllib.parse.urlencode(params)))


def iso_duration(d):
    """PT1H2M3S -> seconds"""
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d or "")
    if not m:
        return 0
    dd, h, mi, s = (int(x or 0) for x in m.groups())
    return dd * 86400 + h * 3600 + mi * 60 + s


def mmss(sec):
    return f"{sec // 60}:{sec % 60:02d}"


def load_previous():
    try:
        txt = open(OUT, encoding="utf-8").read().strip()
        return json.loads(txt[len(PREFIX):].rstrip(";"))
    except Exception:
        return {}


def known_ids():
    html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    block = html.split("const RAW=[", 1)[1].split("];", 1)[0]
    return set(re.findall(r'^\["([\w-]{11})"', block, re.M))


def from_api(key, known):
    ch = api("channels", key, part="statistics,contentDetails", id=CHANNEL_ID)["items"][0]
    st = ch["statistics"]
    uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, token = [], None
    while True:
        p = {"part": "contentDetails", "playlistId": uploads, "maxResults": 50}
        if token:
            p["pageToken"] = token
        page = api("playlistItems", key, **p)
        ids += [it["contentDetails"]["videoId"] for it in page.get("items", [])]
        token = page.get("nextPageToken")
        if not token:
            break
    views, new = {}, []
    for i in range(0, len(ids), 50):
        batch = api("videos", key, part="statistics,contentDetails,snippet", id=",".join(ids[i:i + 50]))
        for v in batch.get("items", []):
            vid = v["id"]
            views[vid] = int(v.get("statistics", {}).get("viewCount", 0))
            sn = v.get("snippet", {})
            sec = iso_duration(v.get("contentDetails", {}).get("duration"))
            if (vid not in known and sn.get("publishedAt", "") > SNAPSHOT
                    and sn.get("liveBroadcastContent", "none") == "none" and sec > 60):
                new.append({"id": vid, "title": sn.get("title", ""), "published": sn.get("publishedAt"),
                            "views": views[vid], "duration": mmss(sec)})
    new.sort(key=lambda x: x["published"])
    return {"subscribers": int(st.get("subscriberCount", 0)), "views": int(st.get("viewCount", 0)),
            "videoCount": int(st.get("videoCount", 0)), "videoViews": views, "newVideos": new}


def from_rss(known):
    ns = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015",
          "media": "http://search.yahoo.com/mrss/"}
    # YouTube's feed sometimes answers 404 for a while; try both feed addresses a few times
    urls = ["https://www.youtube.com/feeds/videos.xml?channel_id=" + CHANNEL_ID,
            "https://www.youtube.com/feeds/videos.xml?playlist_id=UU" + CHANNEL_ID[2:]]
    body, last = None, None
    for attempt in range(3):
        for url in urls:
            try:
                body = get(url)
                break
            except Exception as ex:
                last = ex
        if body:
            break
        time.sleep(5 * (attempt + 1))
    if not body:
        raise last
    root = ET.fromstring(body)
    views, new = {}, []
    for e in root.findall("a:entry", ns):
        vid = e.findtext("yt:videoId", default="", namespaces=ns)
        if not vid:
            continue
        stat = e.find("media:group/media:community/media:statistics", ns)
        n = int(stat.get("views", 0)) if stat is not None else 0
        if n:
            views[vid] = n
        link = (e.find("a:link", ns).get("href", "") if e.find("a:link", ns) is not None else "")
        pub = e.findtext("a:published", default="", namespaces=ns)
        if vid not in known and pub > SNAPSHOT and "/shorts/" not in link:
            new.append({"id": vid, "title": e.findtext("a:title", default="", namespaces=ns),
                        "published": pub, "views": n, "duration": None})
    new.sort(key=lambda x: x["published"])
    return {"videoViews": views, "newVideos": new}


def main():
    prev = load_previous()
    known = known_ids()
    key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = dict(prev)
    try:
        if key:
            fresh = from_api(key, known)
            data.update(fresh)
            data["statsUpdated"] = now
            data["source"] = "YouTube Data API"
        else:
            fresh = from_rss(known)
            data["videoViews"] = {**prev.get("videoViews", {}), **fresh["videoViews"]}
            old_new = {v["id"]: v for v in prev.get("newVideos", [])}
            for v in fresh["newVideos"]:
                old_new[v["id"]] = {**old_new.get(v["id"], {}), **{k: x for k, x in v.items() if x is not None}}
            data["newVideos"] = sorted(old_new.values(), key=lambda x: x.get("published", ""))
            data["source"] = data.get("source") or "RSS feed"
            print("No YOUTUBE_API_KEY secret: refreshed recent videos from the RSS feed only.")
    except Exception as ex:  # keep the site's data as it was
        print(f"Could not reach YouTube ({ex}); keeping the previous data.", file=sys.stderr)
        return 0
    data["updated"] = now
    data["channelId"] = CHANNEL_ID
    order = ["updated", "statsUpdated", "source", "channelId", "subscribers", "views", "videoCount", "newVideos", "videoViews"]
    out = {k: data[k] for k in order if k in data}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("/* Written by .github/scripts/update_channel.py once a day. Don't edit by hand. */\n")
        f.write(PREFIX + json.dumps(out, ensure_ascii=False, indent=1).replace("</", "<\\/") + ";\n")
    print(f"Wrote {OUT}: {len(out.get('videoViews', {}))} view counts, {len(out.get('newVideos', []))} new videos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
