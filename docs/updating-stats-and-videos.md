# Updating channel numbers and videos

The numbers on the site are typed in by hand. They were taken from the YouTube channel on **Nov 13, 2026**. The site doesn't fetch live numbers.

## Headline numbers (hero)

Search `index.html` for `n_learners`. The row under it has subscribers, total views, number of tutorials and first upload date:

```html
<td><strong>46.8K</strong><small>subscribers</small></td>
<td><strong>2.32M</strong><small>views</small></td>
```

Also search for `library_size`, which shows the exact view count.

When you update these, update the date in the footer too: search for `Every number comes from the YouTube channel on`.

## Adding a new video to the atlas

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

## Updating view counts

Change the number in each video's line. The atlas, cluster totals and trajectory stats all recalculate from these.

## Making it automatic later

If you'd rather not update by hand, a small GitHub Action can call the YouTube Data API once a day and rewrite these numbers. That needs a YouTube API key stored as a repository secret. Ask an agent to set it up using `AGENTS.md` for context.
