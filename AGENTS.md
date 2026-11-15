# AGENTS.md

Context for AI agents (Claude Code, Codex, Cursor and others) working on this repository.

## What this repo is

The Bioinformagician website, served by GitHub Pages at https://bioinformagician.info.
It promotes the @Bioinformagician YouTube channel by Khushbu Patel and tells the channel's story as a single-cell experiment.

- `index.html` is the whole homepage: HTML, CSS and JavaScript in one file, no build step.
- `carousels/` holds LinkedIn carousel and guide PDFs plus `carousels.json`, which the Library section reads.
- `CNAME` sets the custom domain. It must stay `bioinformagician.info`.
- `data/channel.js` is generated daily by `.github/workflows/update-channel.yml` running `.github/scripts/update_channel.py` (standard-library Python). It sets `window.CHANNEL`; `index.html` merges it into `RAW` (view counts, new uploads) and the `data-ch` elements, and falls back to the typed-in Nov 13, 2026 snapshot when it's missing. Never hand-edit it or commit an API key; the key lives only in the `YOUTUBE_API_KEY` repo secret. See `docs/updating-stats-and-videos.md`. Because the bot commits daily, `git pull --rebase` before pushing.
- `404.html` is a small self-contained not-found page in the same tokens and fonts. Keep it in sync if the palette changes.
- `_config.yml` is a leftover from the old Jekyll site. The old blog, sign-in and sign-up pages and their assets were removed on Nov 15, 2026; don't bring them back.

## Before you change anything

1. Read `.claude/skills/bioinformagician-design/SKILL.md`. It holds every design rule: colors, type, layout, components, motion and copy voice.
2. Read `docs/` for how each section is built and how to change it.
3. Keep changes small and in the style already there. The owner has rejected redesigns twice; "change only what was asked" is the standing rule.

## Hard rules

- One file, no frameworks, no build tools, no npm. Plain HTML, CSS and vanilla JS.
- Never hardcode a color in new CSS. Use the tokens on `:root` and redefine them for dark mode in both dark blocks (the `prefers-color-scheme` block and `:root[data-theme="dark"]`).
- Keep the UMAP cluster colors (`--A --C --G --T --V --Q --S`) exactly as they are. They are part of the brand.
- External scripts and fonts: Google Fonts only. Everything else is inline.
- Write copy in Khushbu's first-person voice: plain, warm, specific. No em dashes, no hype words, nothing that reads as AI-written.
- The page must work at phone width (360px) with no horizontal scroll, and in light and dark mode.
- Do not remove `CNAME` or change the domain.

## How to check your work

There is no test suite. Open `index.html` in a browser (or run `python3 -m http.server` in the repo and open http://localhost:8000 so `carousels/carousels.json` loads), then:

- Click through every nav link and section.
- Toggle the theme button (brightfield / darkfield).
- Open a Library card and flip pages.
- Check the browser console for errors.
- Resize to phone width.

## Deploying

Push to `main`. GitHub Pages publishes within a minute or two. See `docs/deploy-and-domain.md`.
