---
name: bioinformagician-design
description: Design system and UI/UX rules for the Bioinformagician website (bioinformagician.info). Load before changing anything visual in index.html, adding a section, writing copy, or making a new page in this brand.
---

# Bioinformagician design system

The site sells one idea: **the channel, analyzed like a single-cell experiment.** Every section borrows a real bioinformatics object (a sequencing read, a UMAP, a pseudotime trajectory, a lab protocol, a GenBank record, a protein interactome, a data deposit). New work should extend that metaphor, not break it.

## 1. Concept and page flow

The page is a guided experiment in six numbered steps. Each section opens with a handwritten step label in `.hand`, an `<h2>`, and a short `.lede`.

| Order | id | Step label | Metaphor | What it shows |
|---|---|---|---|---|
| Hero | `#top` | none | One single-cell read decoded | Barcode = BIOINFORMAGICIAN, UMI = KHUSHBUPATEL, the coral wizard hat with a DNA helix |
| 1 | `#atlas` | step 1 · cluster | UMAP atlas | Every video is a cell, colored by topic cluster; search and click a cluster |
| 2 | `#trajectory` | step 2 · order cells in pseudotime | Trajectory + pipeline | Channel eras over time, with QC stats per era |
| 3 | `#protocols` | step 3 · pick a protocol | Lab protocol | Five learning paths with tickable steps saved in localStorage |
| notes | `#library` | lab notebook · notes to keep | Shelf of decks | LinkedIn carousels, PDF guides and the Starter Pack |
| 4 | `#reference` | step 4 · annotate the reference | GenBank record | Khushbu's photo beside a GenBank-style profile |
| 5 | `#interactome` | step 5 · map the interactions | Protein network | Partners, platforms and community |
| 6 | `#deposit` | step 6 · deposit your results | Data deposit | Join the community: YouTube, Follow me on LinkedIn, other links |

## 2. Color

All color comes from CSS custom properties on `:root`. Dark mode ("darkfield") redefines the same names twice: once in `@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){...}}` and once in `:root[data-theme="dark"]{...}`. Any new token goes in all three places.

### Light ("brightfield")

| Token | Value | Use |
|---|---|---|
| `--bg` | `#FBFBFA` | Page background |
| `--surface` | `#FFFFFF` | Cards, panels |
| `--surface-2` | `#F3F6F6` | Insets, chips, photo frame fill |
| `--ink` | `#17232A` | Body text, headings |
| `--ink-2` | `#3C4A51` | Secondary text, ledes |
| `--ink-3` | `#5D6A70` | Captions, meta |
| `--line` | `#E6EBEB` | Borders, rules |
| `--accent` / `--wm` | `#0B5468` | Petrol: primary buttons, links, wordmark |
| `--on-accent` | `#FFFFFF` | Text on petrol |
| `--coral` / `--peach` | `#EE6457` | Brand coral: the hat, highlights, gradient end |
| `--hand` | `#B9432F` | Handwritten step labels and notes |
| `--band` / `--band-2` | `#034C5F` / `#0B5468` | Deep petrol bands (deposit card, hero stage) |
| `--grad-a` → `--grad-b` | petrol → coral | Headline `<em>` gradient text |
| Tints | `--aqua #E3F3F0`, `--blush #FDE9E5`, `--harbor #E2EEF2`, `--lilac #EEEBF6`, `--sand #F5F1E9`, `--sage #E9F1E5` | Library card covers, soft fills |

### Dark ("darkfield")

`--bg #0A0E12`, `--surface #11171C`, `--surface-2 #172128`, `--ink #E8F0F2`, `--ink-2 #B9C7CC`, `--ink-3 #8FA0A8`, `--line #24313A`, `--accent`/`--wm #2FF3D6` (aqua glow), `--on-accent #04201C`, `--hand #FF7A93`, `--coral #FF5E7E`, `--band #06323E`, `--band-2 #0B4A5B`, `--glow: drop-shadow(0 0 5px currentColor)`. Darkfield is meant to feel like fluorescence microscopy: dark stage, glowing marks.

### UMAP cluster palette (do not change)

These are the topic colors in the atlas, protocols and trajectory. They came from Khushbu's original design and are part of the brand.

| Token | Light | Dark | Topic |
|---|---|---|---|
| `--A` | `#F2905C` | `#FFAB7E` | Getting started |
| `--Q` | `#13B99B` | `#19DEBB` | Formats & NGS basics |
| `--C` | `#0B5468` | `#A99BFF` | Bulk RNA-Seq |
| `--V` | `#7083F5` | `#8FA0FF` | Single-cell |
| `--T` | `#F25C80` | `#FF7D98` | Variants & cancer |
| `--G` | `#F2A541` | `#FFBE78` | Regulation |
| `--S` | `#EE7FC3` | `#FF96D5` | Talks & collabs |

Rules: color follows the topic, never the rank. Text never takes a cluster color; a colored dot or mark beside it carries the identity.

### Logo colors

The logo is a coral wizard hat (`#EE6457`) with pale ears `#FCDCD6`, on a petrol stage (`#0B5468` → `#034C5F`), with a pale aqua DNA strand `#BFE8E2`. The hero illustration uses the same colors.

## 3. Typography

Loaded from Google Fonts in one `<link>`.

| Role | Font | Token / class | Notes |
|---|---|---|---|
| Display / headings | Bricolage Grotesque 400/600/800 | `--font-display` | Tight tracking (`-.02em`), big `clamp()` sizes |
| Body | IBM Plex Sans 400/500/600 | `--font-body` | 16px base, comfortable line height |
| Code, data, labels | IBM Plex Mono 400/500/600 | `--font-mono` | Stats, GenBank record, protocol commands, tags |
| Handwritten notes | Caveat 500/700 | `--font-hand`, `.hand` | Step labels and margin notes, in `--hand` color, slight rotation is fine |
| Wordmark | Kalam 700 | `.wm` | "Bioinformagician" with a capital B, in `--wm`, 23px in the nav, 19px in the footer |

Always write the brand as **Bioinformagician** (capital B). The handle is **@Bioinformagician**.

## 4. Layout

- Content sits in `.wrap` (max width ~1200px, side padding `clamp()`, 16px minimum on phones).
- Sections stack vertically with generous padding; each starts with `.sec-head` (step label, h2, lede).
- Cards and panels: `--surface`, 1px `--line` border, radius `--r` (16px). Photo frame: 18px radius, soft petrol shadow.
- Two-column grids collapse to one column under ~860px.
- At 460px and below the nav hides the wordmark and the theme label; the logo image stays.
- No horizontal scroll at any width.

## 5. Components

- **Nav**: logo image (40px, 10px radius) + Kalam wordmark, section links, theme toggle (`brightfield` / `darkfield`), petrol Subscribe button.
- **Buttons**: `.btn` (outline) and `.btn.primary` (petrol fill, white text). Short verb-first labels.
- **Chips**: filter pills with `aria-pressed`.
- **Placeholder**: `.placeholder` dashed box with a `.tag`. Use for content that is not real yet; never ship fake numbers.
- **Library card**: `.lib-item` with a `.lib-cover` deck in a tint color, type and page count on top, title in display font, `@Bioinformagician` at the bottom. Opens `#libViewer` (a `<dialog>`) with page dots, prev/next, Download PDF and View on LinkedIn.
- **GenBank record**: `.panel.gb` in mono, labels in `--C`, placeholders in `--hand`.
- **Tooltips**: on hover over cells and nodes, title in body font, meta line below.

## 6. Interaction and motion

- Everything interactive works with mouse, touch and keyboard. Visible `:focus-visible` outlines.
- Hover reveals detail; click commits (filter a cluster, open a deck).
- Motion is light: the hero read "sequences" letter by letter, the helix rises from the hat, cells fade in. Respect `prefers-reduced-motion`.
- Progress that matters to a visitor (protocol ticks, theme choice) is saved in `localStorage` and wrapped in try/catch.

## 7. Library data (`carousels/carousels.json`)

The Library shows the Starter Pack (Notion link) plus whatever `carousels/carousels.json` lists. While the list is empty, sample placeholder cards show. Format:

```json
[
  {"title": "What's inside a FASTQ file", "file": "carousels/fastq.pdf", "linkedin": "https://www.linkedin.com/posts/...", "pages": 8, "type": "carousel"}
]
```

`type` is `carousel` or `guide`; `linkedin` is optional and must start with `https://`; `pages` drives the page dots.

Covers: a card shows `cover` (the carousel's first slide, a 4:5 JPG in `carousels/covers/`) when present. Items without one (the Starter Pack, PDF guides) use the designed cover `.lib-cover.made`, which mirrors the carousel covers: warm paper `#FAF8F4`, a soft circle in the top-right corner (mint `#CDEFE4` or peach `#F6CFB6`), a mono uppercase kicker, a heavy Bricolage headline with one word highlighted (`#FBD3CC` underlay), a gray sub line and the "Bioinfor**magician**." wordmark (magician in `#0B5468`, dot in `#EE6457`). Covers stay light in dark mode, like printed slides. Entries feed it with `kicker`, `headline`, `mark`, `sub`. With neither, cards fall back to a tinted cover (harbor, blush, sage, lilac, sand, aqua in order).

## 8. Copy voice

- First person, Khushbu speaking: "I put these five paths together from my own videos..."
- Plain and specific. Short sentences. Real numbers with their date.
- Bioinformatics puns are welcome when they explain something (barcode, UMI, pseudotime, deposit). Do not stack them.
- No em dashes, no "unlock", "elevate", "journey" filler, no exclamation marks in headings.
- Headings are statements: "Every tutorial is a cell. Here is the atlas."

## 9. Accessibility checklist

- Text contrast meets WCAG AA in both themes.
- Every image has alt text (decorative ones get `alt=""`).
- SVG charts have an `aria-label` or a text alternative.
- Color is never the only signal: labels or legends always accompany cluster colors.

## 10. Don'ts

- Don't add frameworks, build steps or new external scripts.
- Don't introduce new brand colors or change the cluster palette.
- Don't replace Caveat or Kalam with other script fonts without asking.
- Don't redesign a section when asked for a small change.
