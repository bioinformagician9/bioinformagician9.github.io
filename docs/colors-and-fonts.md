# Colors and fonts

The full design system, with every value, is in `.claude/skills/bioinformagician-design/SKILL.md`. This page covers how to change things.

## Where colors live

At the top of the `<style>` block in `index.html` there are three blocks of color variables:

1. `:root{ ... }`: light mode ("brightfield").
2. `@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){ ... } }`: dark mode when the visitor's computer is in dark mode.
3. `:root[data-theme="dark"]{ ... }`: dark mode when the visitor clicks the theme button.

Blocks 2 and 3 must stay identical. If you change a dark color, change it in both.

## Changing a brand color

Change the variable's value, and every place that uses it updates. The main ones:

| Variable | Light | Dark | Used for |
|---|---|---|---|
| `--accent` | `#0B5468` petrol | `#2FF3D6` aqua | Buttons, links |
| `--wm` | `#0B5468` | `#2FF3D6` | The Bioinformagician wordmark |
| `--coral` | `#EE6457` | `#FF5E7E` | Highlights, gradient |
| `--hand` | `#B9432F` | `#FF7A93` | Handwritten step labels |
| `--bg` | `#FBFBFA` | `#0A0E12` | Page background |
| `--ink` | `#17232A` | `#E8F0F2` | Main text |

## The cluster colors

`--A --C --G --T --V --Q --S` color the topic clusters in the atlas. They're part of the brand, so change them only on purpose. Each cluster's color is set in `const TOPICS` in the script (`c:"--A"` and so on).

## Fonts

All fonts come from one Google Fonts `<link>` in the `<head>`.

| Font | Where |
|---|---|
| Bricolage Grotesque | Headings |
| IBM Plex Sans | Body text |
| IBM Plex Mono | Data, stats, labels |
| Caveat | Handwritten step labels |
| Kalam | The Bioinformagician wordmark in the nav and footer |

To change the wordmark font:

1. Pick a font on https://fonts.google.com and add it to the Google Fonts link (for example `&family=Pacifico`).
2. Search for `.wm{` in the CSS and change `font-family`.

## The logo image

The logo in the nav, footer and browser tab is embedded as text (it starts with `data:image/jpeg;base64,`). To use a file instead, save it as `images/logo.jpg` and replace each `src="data:image/jpeg;base64,..."` that belongs to the logo with `src="images/logo.jpg"`. Search for `class="logo"`, the footer, and `rel="icon"`.
