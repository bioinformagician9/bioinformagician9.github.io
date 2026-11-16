# Library: adding carousels and PDF guides

The Library section shows your Bioinformatics Starter Pack plus every PDF listed in `carousels/carousels.json`. While that list is empty, the Library shows sample cards so the section doesn't look bare. As soon as it has one real entry, the sample cards disappear.

## Add a new carousel

1. Export the carousel from Canva (or wherever you made it) as a PDF.
2. Give it a short file name with no spaces, for example `fastq-basics.pdf`.
3. Upload it to the `carousels/` folder. On github.com: open the repo, click `carousels`, then **Add file → Upload files**.
4. Open `carousels/carousels.json` on github.com and click the pencil icon to edit.
5. Make the card cover: export the carousel's first slide as a JPG about 600 px wide (in Canva: Share → Download → JPG, page 1) and upload it to `carousels/covers/` with the same name as the PDF.
6. Add an entry for it:

```json
[
  {
    "title": "What's inside a FASTQ file",
    "file": "carousels/fastq-basics.pdf",
    "linkedin": "https://www.linkedin.com/posts/your-post-link",
    "pages": 8,
    "type": "carousel",
    "cover": "carousels/covers/fastq-basics.jpg"
  }
]
```

7. Click **Commit changes**. The site updates in a minute or two.

### Page pictures (why the viewer fits phones)

The viewer doesn't show the PDF itself. It shows one picture per page from `carousels/pages/<pdf name>/1.jpg, 2.jpg ...`, which fit any screen and can be swiped on a phone. The **Download PDF** button still gives the real PDF.

You don't make these pictures yourself. When you upload or replace a PDF in `carousels/`, the **Make carousel page pictures** job on the Actions tab makes them and commits them, usually within a minute. Until it finishes, the viewer shows the PDF instead.

To make them on your own computer instead, run `bash .github/scripts/render_carousel_pages.sh` from the repo folder (it needs `pdftoppm`, part of poppler).

## Adding more than one

Separate entries with a comma. The order in the file is the order on the page, so put the newest first if you like.

```json
[
  {"title": "Newest deck", "file": "carousels/newest.pdf", "pages": 10, "type": "carousel"},
  {"title": "Older deck", "file": "carousels/older.pdf", "pages": 8, "type": "carousel"}
]
```

## The fields

| Field | Required | What it does |
|---|---|---|
| `title` | yes | The name on the card and in the viewer |
| `file` | yes | Path to the PDF, starting with `carousels/` |
| `type` | no | `carousel` (default) or `guide`. Controls the filter chips and the label |
| `pages` | no | Number of pages; sets the page dots. Defaults to 1 |
| `linkedin` | no | Link to the LinkedIn post. Must start with `https://`. Adds a View on LinkedIn button |
| `cover` | no | Path to a JPG or PNG of the first slide, used as the card's front |
| `kicker`, `headline`, `mark`, `sub` | no | For a PDF with no cover image (like a guide), the site draws a cover in the same style as the carousels: `kicker` is the small label at the top, `headline` the big title, `mark` one word of the headline to highlight, `sub` a short line under it |

Without `cover` or `headline`, the card falls back to a plain tinted cover with the title.

### Designed cover example (the trim guide)

```json
{"type": "guide", "title": "Should I trim before alignment? A decision tree", "file": "carousels/trim-decision-tree.pdf", "pages": 3,
 "kicker": "NGS decision framework", "headline": "Should I trim before alignment?", "mark": "trim",
 "sub": "Answer three questions. Get a clear call for any pipeline."}
```

## If it doesn't show up

- JSON is strict: every entry needs `{ }`, fields need double quotes, entries need commas between them, and there's no comma after the last one. Paste the file into https://jsonlint.com to check it.
- Check the `file` path matches the PDF's name exactly, including capital letters.
- Hard-refresh the page (Cmd+Shift+R) in case your browser cached the old list.

## Changing the Starter Pack link

Search `index.html` for `Bioinformatics Starter Pack`. The `url` next to it is the Notion link. Its cover text (kicker and line) is in the `card()` function a few lines below, in the `made({...})` call for the starter.
