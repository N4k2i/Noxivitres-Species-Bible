# NOXIVITRES Species Bible — Jekyll Site

A repository-ready Jekyll/GitHub Pages website generated from the complete NOXIVITRES Markdown bible.

## What is included

- 336 encyclopedia entry pages
- 275 technical plate pages
- 18 Part landing pages
- Reference Atlas, rarity hub, Generation Zero hub, founder profiles, complete browser, and client-side search
- Responsive dark/neon custom theme with no third-party front-end framework
- Untouched source bible at `assets/source/NOXIVITRES_SPECIES_BIBLE.md`
- GitHub Actions workflow for GitHub Pages
- Regeneration and integrity scripts in `scripts/`

## Publish on GitHub Pages

1. Create a repository and upload the contents of this folder to the repository root.
2. Push to the `main` branch.
3. In **Settings → Pages → Build and deployment → Source**, choose **GitHub Actions**.
4. The included `.github/workflows/pages.yml` workflow builds Jekyll and deploys the site.

If you are publishing as a project site such as `username.github.io/repository-name`, GitHub Pages' `configure-pages` action supplies the deployment base path during the Actions build. The templates use Jekyll's `relative_url` filter so navigation remains base-path aware.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Then open the local URL Jekyll prints (normally `http://127.0.0.1:4000`).

## Regenerating the split reference pages

The generated collection pages are intentionally committed so GitHub can build the site without a custom Jekyll plugin. The complete source Markdown is also retained for auditability.

Run:

```bash
python scripts/verify_integrity.py
```

before publishing after major manual edits.

## Canon notes

- Common through Mythic are open.
- Unobtanium is creator-locked.
- Riven Solace is owned by `@n4k2` on Discord.
- Blade is owned by `@altblade` on Discord.
- Species openness does not transfer character ownership.
