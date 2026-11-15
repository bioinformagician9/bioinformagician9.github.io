# Carousels for the Library

Drop a PDF in this folder, then add one entry for it to `carousels.json`. The Library on the site picks it up on the next page load.

```json
[
  {
    "title": "What's inside a FASTQ file",
    "file": "carousels/fastq.pdf",
    "linkedin": "https://www.linkedin.com/posts/...",
    "pages": 8,
    "type": "carousel",
    "cover": "carousels/covers/fastq.jpg"
  }
]
```

- `type` is `carousel` or `guide`.
- `linkedin` is optional.
- `cover` is the first slide as a JPG in `covers/`; it becomes the card's front.
- A guide with no cover image can use `kicker`, `headline`, `mark` and `sub` to get a designed cover. See `docs/library-and-carousels.md`.
- While the list is empty (`[]`), the Library shows the sample cards. Once it has at least one entry, your real PDFs replace them.
