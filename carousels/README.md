# Carousels for the Library

The Library on the site reads `carousels.json`. To add a new carousel:

1. **PDF:** upload it to this folder with a short name and no spaces, numbered after the last one, for example `10-bam-files.pdf`.
2. **Cover:** upload its first slide as a JPG about 600 px wide to `covers/`, with the same name (`covers/10-bam-files.jpg`).
3. **Entry:** add one line at the **top** of `carousels.json` (newest first), followed by a comma:

```json
[
  {"type": "carousel", "title": "BAM files, explained", "file": "carousels/10-bam-files.pdf", "linkedin": "https://www.linkedin.com/posts/...", "pages": 9, "cover": "carousels/covers/10-bam-files.jpg"},
  {"type": "carousel", "title": "Blood vs saliva vs tumor: why sample type matters", ...}
]
```

That's it. Within a minute or two:

- the **Make carousel page pictures** job turns the PDF's pages into pictures in `pages/<pdf name>/` for the viewer (nothing to do yourself);
- the site shows the new card first, and the Library splits into pages on its own (8 cards per page on wide screens, 6 on tablets and phones), with Prev, page numbers and Next under the cards.

Fields:

- `type` is `carousel` or `guide`.
- `pages` is the number of slides.
- `linkedin` is optional and must start with `https://`.
- `cover` is the first slide as a JPG in `covers/`; it becomes the card's front. To make it on your computer: `pdftoppm -jpeg -f 1 -l 1 -singlefile -scale-to-x 600 -scale-to-y -1 carousels/10-bam-files.pdf carousels/covers/10-bam-files`.
- A guide with no cover image can use `kicker`, `headline`, `mark` and `sub` to get a designed cover. See `docs/library-and-carousels.md`.
- The order in the file is the order on the site. Guides sit at the end.
