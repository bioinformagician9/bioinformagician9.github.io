# Bioinformagician website

The homepage for the @Bioinformagician YouTube channel, live at **https://bioinformagician.info**.

It tells the channel's story as a single-cell experiment: every video is a cell in a UMAP atlas, the channel's history is a pseudotime trajectory, learning paths are lab protocols, and the About section is a GenBank record.

## What's in this repo

| Path | What it is |
|---|---|
| `index.html` | The whole homepage. HTML, CSS and JavaScript in one file. No build step. |
| `carousels/` | Your LinkedIn carousel and guide PDFs, plus `carousels.json`, the list the Library reads. |
| `CNAME` | Tells GitHub Pages to serve the site on `bioinformagician.info`. Don't delete it. |
| `docs/` | Step-by-step guides for making changes yourself. |
| `AGENTS.md` | Instructions for AI coding agents working on this repo. |
| `.claude/skills/bioinformagician-design/SKILL.md` | The full design system: colors, fonts, layout, components, copy voice. |
| `404.html` | The page shown for an address that doesn't exist. Self-contained, same colors and fonts. |
| `_config.yml` | Leftover setting from the old Jekyll site. Harmless. |

## Common changes

| I want to... | Guide |
|---|---|
| Add a LinkedIn carousel or PDF guide | [docs/library-and-carousels.md](docs/library-and-carousels.md) |
| Change text in a section | [docs/editing-sections.md](docs/editing-sections.md) |
| Add a new video or update the channel numbers | [docs/updating-stats-and-videos.md](docs/updating-stats-and-videos.md) |
| Change a color or font | [docs/colors-and-fonts.md](docs/colors-and-fonts.md) |
| Publish changes, or fix the domain | [docs/deploy-and-domain.md](docs/deploy-and-domain.md) |

## Previewing locally

Double-clicking `index.html` works for most things. The Library can only read `carousels/carousels.json` when the page is served, so for a full preview run this in the repo folder:

```
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Publishing

Commit and push to the `main` branch. GitHub Pages rebuilds the site in a minute or two. Details are in [docs/deploy-and-domain.md](docs/deploy-and-domain.md).
