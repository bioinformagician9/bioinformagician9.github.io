# Carousels for the Library

Drop a PDF in this folder, then add one entry for it to `carousels.json`. The Library on the site picks it up on the next page load.

```json
[
  {
    "title": "What's inside a FASTQ file",
    "file": "carousels/fastq.pdf",
    "linkedin": "https://www.linkedin.com/posts/...",
    "pages": 8,
    "type": "carousel"
  }
]
```

- `type` is `carousel` or `guide`.
- `linkedin` is optional.
- While the list is empty (`[]`), the Library shows the sample cards. Once it has at least one entry, your real PDFs replace them.
