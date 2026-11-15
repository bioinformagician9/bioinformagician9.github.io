# Updating channel numbers and videos

## What updates by itself

A GitHub Action, **Update YouTube numbers** (`.github/workflows/update-channel.yml`), runs every day at 09:17 UTC. It writes `data/channel.js`, and the page reads that file when it loads:

| With the `YOUTUBE_API_KEY` secret | Without it |
|---|---|
| Subscribers, total views and video count in the hero, the GenBank record, the community map and step 6 | Stay at the Nov 13, 2026 numbers typed into `index.html` |
| View counts for every video in the atlas and trajectory | View counts for the 15 newest videos only (from the public RSS feed) |
| New uploads (longer than a minute, not live streams) added as cells, with their real length | New uploads added, with a placeholder length of 10:00 |
| Footer says "Numbers refresh daily from YouTube. Last updated …", with the date in the visitor's own time zone | Footer keeps "Every number comes from the YouTube channel on Nov 13, 2026." |

In practice YouTube's public feed often answers "not found" to GitHub's servers (it did on the first runs, Nov 15, 2026), so without the key the job usually finds nothing and the site keeps its snapshot. The key is what makes the refresh reliable.

If YouTube can't be reached, the job keeps yesterday's data and doesn't fail. If `data/channel.js` is missing, the page shows the typed-in snapshot.

New uploads get a topic guessed from the title (single-cell, variants, RNA-Seq, regulation, formats, talks, otherwise getting started). To fix a guess or a title, copy the video into `const RAW=[` by hand (see below): a video in `RAW` always keeps your topic. New videos join the last era of the trajectory; add a new era to `const ERAS=[` when a new chapter starts.

### Turn on the full numbers: add a free YouTube API key (about 5 minutes)

1. Go to https://console.cloud.google.com and sign in with the Google account you want to own the key.
2. Create a project (top bar → project picker → **New project**), for example `bioinformagician-site`.
3. Open **APIs & Services → Library**, search for **YouTube Data API v3**, and click **Enable**.
4. Open **APIs & Services → Credentials → Create credentials → API key**.
5. Click the new key to edit it. Under **API restrictions** choose **Restrict key**, tick **YouTube Data API v3**, and **Save**. Leave application restrictions on **None** (the job runs on GitHub's servers).
6. Copy the key.
7. In the GitHub repo, go to **Settings → Secrets and variables → Actions → New repository secret**. Name it exactly `YOUTUBE_API_KEY`, paste the key, and click **Add secret**.
8. Go to **Actions → Update YouTube numbers → Run workflow** to refresh right away instead of waiting for tomorrow.

The key is free and needs no billing: the job uses a handful of the 10,000 daily quota units. Secrets are never shown on the site or in the logs. To stop using it, delete the secret; to rotate it, make a new key and replace the secret.

### Run it by hand or change the time

- **Run now:** Actions tab → **Update YouTube numbers** → **Run workflow**.
- **Change the time:** edit the `cron` line in `.github/workflows/update-channel.yml` (it's in UTC).
- **Pause it:** Actions tab → the workflow → **⋯ → Disable workflow**.
- GitHub pauses scheduled jobs after 60 days with no activity in a repo. The daily commit counts as activity, so this shouldn't happen, but if it does, re-enable it from the same menu.

## Changing the typed-in snapshot

The numbers in `index.html` are the fallback. They were taken from the YouTube channel on **Nov 13, 2026**.

### Headline numbers (hero)

Search `index.html` for `n_learners`. The row under it has subscribers, total views, number of tutorials and first upload date:

```html
<td><strong data-ch="subs">46.8K</strong><small>subscribers</small></td>
<td><strong data-ch="views">2.32M</strong><small>views</small></td>
```

Also search for `library_size`, which shows the exact view count. Anything marked `data-ch` is overwritten by the daily data when it has those numbers.

When you update these, update the date in the footer too: search for `Every number comes from the YouTube channel on`.

### Adding a video to the atlas by hand

Search for `const RAW=[`. Each video is one line:

```js
["VIDEO_ID","Video title",VIEWS,"MM:SS",YEARS_AGO,"topic"],
```

| Part | Example | Meaning |
|---|---|---|
| `VIDEO_ID` | `2RFYKTvCXHs` | The part after `watch?v=` in the YouTube link |
| title | `How to download RNA-Seq data from NCBI GEO` | Shown in tooltips and lists |
| `VIEWS` | `147000` | A plain number, no commas |
| `"MM:SS"` | `"9:02"` | Video length |
| `YEARS_AGO` | `4` | Whole years since upload; `0` shows "this year" |
| topic | `rna` | One of the cluster keys below |

Topic keys and their cluster colors:

| Key | Label |
|---|---|
| `start` | Getting started |
| `formats` | Formats & NGS basics |
| `rna` | Bulk RNA-Seq |
| `sc` | Single-cell |
| `var` | Variants & cancer |
| `epi` | Regulation |
| `talk` | Talks & collabs |

The list is in upload order, oldest first. Add new videos at the end, before the closing `];`.

If you add videos, also check `const ERAS=[`: the last era's `to` value is the position of the last video it covers (counting from 0). Raise it so the new videos belong to an era.

### Updating view counts by hand

Change the number in each video's line. The atlas, cluster totals and trajectory stats all recalculate from these.

