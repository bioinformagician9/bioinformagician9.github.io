# Editing sections

Everything lives in `index.html`. Use your editor's search (Cmd+F) to jump to the text you want to change.

## How the file is laid out

1. `<head>`: page title, description, fonts, and one big `<style>` block with all the CSS.
2. `<nav>`: logo, wordmark, section links, theme toggle, Subscribe button, and the section menu button.
3. `<header class="hero" id="top">`: the decoded sequencing read and the wizard hat.
4. One `<section id="...">` per step, in page order:
   - `#atlas`: step 1, the UMAP of all videos
   - `#trajectory`: step 2, the channel's eras over time
   - `#protocols`: step 3, the five learning paths
   - `#library`: lab notebook, carousels and guides
   - `#reference`: step 4, your photo and GenBank-style profile
   - `#interactome`: step 5, partners and community
   - `#deposit`: step 6, ways to follow and connect
5. `<footer>`
6. One `<script>` block at the end with all the JavaScript, including the data lists.

## Changing a heading or intro paragraph

Each section starts like this:

```html
<div class="sec-head">
  <span class="hand">step 3 · pick a protocol</span>
  <h2>Your learning path, written like a lab protocol.</h2>
  <p class="lede">I put these five paths together from my own videos...</p>
</div>
```

Edit the text between the tags. Keep the `class` names as they are.

## Changing the hero

Search for `<h1>`. The headline is `Raw reads in. <em>Real understanding</em> out.` The words inside `<em>` get the petrol-to-coral gradient.

## Changing your photo (step 4)

Search for `class="portrait photo"`. The `src` is the image itself, embedded as text (it starts with `data:image/jpeg;base64,`). The easiest way to swap it:

1. Save your new photo as `images/khushbu.jpg` (a portrait crop, about 480 x 600 px, under 150 KB).
2. Replace the whole `src="data:image/jpeg;base64,..."` with `src="images/khushbu.jpg"`.

## Changing the GenBank profile (step 4)

Search for `class="panel gb"`. Each line is:

```html
<div class="ln"><span>LABEL</span><span>value</span></div>
```

Lines with `class="ph"` are placeholders (shown in the handwriting color). Replace the text and remove `ph` once it's real.

- Write each value as one line of text. The browser wraps long values under the value column, like a GenBank record, so don't add manual line breaks.
- Qualifier lines under FEATURES (mission, motto, data, origin) use `class="ln q2"`, which indents the label.
- The LOCUS value uses `class="pw"` so the wide gaps between its fields are kept. `data-ch="count"` on the tutorial number is filled in by the daily refresh.
- On phones (600px and under) the label column narrows and the text gets slightly smaller, so the record never runs off the screen.

## Changing the learning paths (step 3)

Search for `const P=[` in the script. Each path is one object with:

- `tab`: the tab label
- `cmd`: the fake command shown under the title
- `level`, `title`, `text`: what the card says
- a list of steps, each pointing to a video

Keep the same shape when you add or remove a path.

## Changing the channel eras (step 2)

Search for `const ERAS=[`. Each era has `from` and `to` (video positions in the video list, counting from 0), a `name`, `years` and a `text` paragraph.

## Changing the follow links (step 6)

Search for `step 6 · deposit your results`. Each link is an `<li>` with an `<a href="...">`. Change the `href` and the text inside `<b>` and the `<span>` under it.

## Changing the nav links

There are two sets of links, and both point to section ids:

- The short links across the top on wide screens. Search for `<li><a href="#atlas">Atlas</a></li>`.
- The section menu behind the round button with three lines (the hamburger), shown on every screen size. Search for `id="secMenu"`. Each item is an `<li>` with a number in `<b>`, the name in `<span>` and a one-line hint in `<small>`.

When you add, remove or rename a section, update both.

## Things to avoid

- Don't delete a `<section>` without also removing its nav link and its item in the section menu.
- Don't rename `id`s or `class`es; the CSS and JavaScript look for them.
- Don't paste text with em dashes or smart quotes from Word if you can avoid it; plain quotes are safest in HTML.
- After editing, open the page and check the browser console (right-click, Inspect, Console) for red errors.
