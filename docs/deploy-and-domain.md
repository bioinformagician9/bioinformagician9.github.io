# Publishing and the domain

## How publishing works

This repo is a GitHub Pages site. Whatever is on the `main` branch is the live site. Every push to `main` republishes it, usually within 1 to 2 minutes. You can watch progress under the repo's **Actions** tab ("pages build and deployment").

## Editing on github.com (no tools needed)

1. Open the file on github.com and click the pencil icon.
2. Make the change.
3. Click **Commit changes**, keep "Commit directly to the main branch", and confirm.

## Editing on your computer

```
git clone https://github.com/bioinformagician9/bioinformagician9.github.io
cd bioinformagician9.github.io
# make your changes, preview with: python3 -m http.server 8000
git add .
git commit -m "Describe the change"
git push
```

The **Update YouTube numbers** action commits `data/channel.js` to `main` once a day. If you keep a copy on your computer, run `git pull` before you start editing, or your push will be rejected.

## Undoing a change

On github.com, open **Commits**, find the commit, and use **Revert**. Or locally: `git revert <commit-id>` then `git push`.

## The custom domain

The site is served on **bioinformagician.info**, registered at Squarespace.

### In this repo

`CNAME` contains `bioinformagician.info`. Don't delete or rename it, or GitHub Pages will drop the custom domain.

### In GitHub (Settings → Pages)

- **Source**: Deploy from a branch, `main`, `/ (root)`.
- **Custom domain**: `bioinformagician.info`.
- **Enforce HTTPS**: on. GitHub can only turn this on after DNS is working and it has issued a certificate, which can take up to 24 hours after a DNS change.

### In Squarespace (Domains → bioinformagician.info → DNS)

Custom records:

| Type | Name | Data |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | bioinformagician9.github.io |

The "Squarespace Defaults" preset was removed, because its records point the domain at Squarespace's own hosting. Don't add it back. The "Squarespace Domain Connect" and "Email Security" presets are fine to keep.

These IP addresses are GitHub's. If GitHub ever changes them, its docs ("Managing a custom domain for your GitHub Pages site") will list the new ones.

### If the site doesn't load on the domain

1. In Settings → Pages, check the custom domain shows `bioinformagician.info` with a green "DNS check successful".
2. If it says the DNS check failed, compare the Squarespace records with the table above.
3. DNS changes can take a few hours to spread. https://dnschecker.org shows what the world currently sees.
4. If HTTPS shows a certificate warning, wait a few hours, then in Settings → Pages untick and re-tick **Enforce HTTPS**.
