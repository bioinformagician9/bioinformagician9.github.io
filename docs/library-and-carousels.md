# Library: adding carousels and PDF guides

The Library section shows your Bioinformatics Starter Pack plus every PDF listed in `carousels/carousels.json`. While that list is empty, the Library shows sample cards so the section doesn't look bare. As soon as it has one real entry, the sample cards disappear.

## Add a new carousel

1. Export the carousel from Canva (or wherever you made it) as a PDF.
2. Give it a short file name with no spaces, for example `fastq-basics.pdf`.
3. Upload it to the `carousels/` folder. On github.com: open the repo, click `carousels`, then **Add file → Upload files**.
4. Open `carousels/carousels.json` on github.com and click the pencil icon to edit.
5. Add an entry for it:

```json
[
  {
    "title": "What's inside a FASTQ file",
    "file": "carousels/fastq-basics.pdf",
    "linkedin": "https://www.linkedin.com/posts/your-post-link",
    "pages": 8,
    "type": "carousel"
  }
]
```

6. Click **Commit changes**. The site updates in a minute or two.

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

## If it doesn't show up

- JSON is strict: every entry needs `{ }`, fields need double quotes, entries need commas between them, and there's no comma after the last one. Paste the file into https://jsonlint.com to check it.
- Check the `file` path matches the PDF's name exactly, including capital letters.
- Hard-refresh the page (Cmd+Shift+R) in case your browser cached the old list.

## Changing the Starter Pack link

Search `index.html` for `Bioinformatics Starter Pack`. The `url` next to it is the Notion link.
