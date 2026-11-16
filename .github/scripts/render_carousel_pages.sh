#!/usr/bin/env bash
# Turns each PDF in carousels/ into one JPG per page, in carousels/pages/<pdf name>/1.jpg, 2.jpg ...
# The Library viewer shows these pictures, which fit any screen (phones included).
# A PDF whose pages already exist and are not older than the PDF is skipped.
# Needs poppler-utils (pdftoppm). Run from the repo root: bash .github/scripts/render_carousel_pages.sh
set -euo pipefail
shopt -s nullglob
for pdf in carousels/*.pdf; do
  name=$(basename "$pdf" .pdf)
  out="carousels/pages/$name"
  if [ -f "$out/1.jpg" ] && [ ! "$pdf" -nt "$out/1.jpg" ]; then continue; fi
  rm -rf "$out"; mkdir -p "$out"
  pdftoppm -jpeg -jpegopt quality=82,optimize=y -scale-to-x 1080 -scale-to-y -1 "$pdf" "$out/p"
  # pdftoppm names pages p-01.jpg or p-1.jpg; rename them to 1.jpg, 2.jpg ...
  for f in "$out"/p-*.jpg; do n=${f##*/p-}; n=${n%.jpg}; mv "$f" "$out/$((10#$n)).jpg"; done
  echo "rendered $pdf -> $out ($(ls "$out" | wc -l) pages)"
done
