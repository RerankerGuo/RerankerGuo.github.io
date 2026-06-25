# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Jekyll-based academic personal homepage for **Ziyang Guo (郭子扬)**, forked from [RayeRen/acad-homepage.github.io](https://github.com/RayeRen/acad-homepage.github.io) (the "AcadHomepage" template) and migrated to the `RerankerGuo` GitHub account. The site is hosted at `https://RerankerGuo.github.io`.

The site has two distinguishing features beyond a vanilla Jekyll template:
1. **Auto-refreshing Google Scholar citations** via a Python crawler + GitHub Action.
2. **Per-paper citation counts** rendered client-side from a JSON file on a separate branch.

## Local Development

```bash
bash run_server.sh        # runs `bundle exec jekyll liveserve` → http://127.0.0.1:4000
```

Requires Ruby + Bundler. First run: `bundle install`. The `_config.yml` is **not** auto-reloaded by `jekyll serve` — restart the server after editing it.

`_site/` is the build output and is gitignored.

## Architecture

### Content vs. layout separation

| Layer | Location | Edit when… |
|---|---|---|
| Site-wide config | `_config.yml` | Author info, repo URL, analytics IDs, plugins, SEO verifications |
| Single-page content | `_pages/about.md` | Anything a visitor reads (bio, news, projects, awards) |
| Sidebar nav links | `_data/navigation.yml` | Adding/removing top-nav anchors |
| Styling | `_sass/*.scss` (compiled into `_sass/_base.scss` etc.) | Visual changes — `_sidebar.scss` is the most recently customized file |
| Page chrome | `_layouts/default.html` + `_includes/*.html` | Header, sidebar, scripts, SEO meta |

`_config.yml` sets `defaults` so every page under `_pages/` gets `layout: default` and `author_profile: true` automatically.

### Google Scholar citation pipeline (the non-Jekyll half)

Two independent pieces run on different schedules and live in different branches:

1. **`google_scholar_crawler/main.py`** — Python script using `scholarly` + `jsonpickle`. Reads `GOOGLE_SCHOLAR_ID` env var, fetches the author profile, and writes two JSON files to `results/`:
   - `gs_data.json` — full profile incl. publications keyed by `author_pub_id`
   - `gs_data_shieldsio.json` — `{ "schemaVersion": 1, "label": "citations", "message": "<citedby>" }` for shield-style badges

2. **`.github/workflows/google_scholar_crawler.yaml`** — runs on `page_build` and daily at `08:00 UTC`. Executes `main.py`, then force-pushes `results/*.json` to the **`google-scholar-stats` branch** (note: this is a branch, not a folder in `main`). The script **exits 0 silently** when `GOOGLE_SCHOLAR_ID` is unset, so missing-secret builds don't fail.

### Citation rendering on the page

The frontend never blocks on the citation JSON:

- `_config.yml` toggles `google_scholar_stats_use_cdn` (default `true`) — when on, the page reads from `cdn.jsdelivr.net/gh/{repository}@google-scholar-stats/...` instead of `raw.githubusercontent.com`.
- `_includes/fetch_google_scholar_stats.html` (loaded via `_layouts/default.html`) does the `$.getJSON` and writes the total into `#total_cit`.
- To show a per-paper citation count, drop `<span class='show_paper_citations' data='AUTHOR_PUB_ID'></span>` into `_pages/about.md`. The `AUTHOR_PUB_ID` is the value of `citation_for_view=...` from the paper's Google Scholar URL.

### Fork-specific deviations from upstream AcadHomepage

- `site.repository` in `_config.yml` is `RerankerGuo/RerankerGuo.github.io` — **must stay in sync with the actual GitHub repo name** or the CDN citation URLs 404.
- `_config.yml` adds the `hawkins` gem alongside the standard Jekyll plugins.
- `_sass/_sidebar.scss` was restyled locally (see commit `5afbafd`).
- `google_scholar_crawler/main.py` was patched (commit `042bece`) to skip cleanly when the secret is absent rather than crashing.
- Sidebar profile (`_includes/author-profile.html`) and SEO include (`_includes/seo.html`) have minor local tweaks.

## Common Tasks

**Update author info or social links** → `_config.yml` under `author:`.
**Edit page content** → `_pages/about.md` (single page; `permalink: /`).
**Add a nav anchor** → `_data/navigation.yml`, then put a matching `<span class='anchor' id='anchor-id'></span>` in `_pages/about.md`.
**Change a color/layout detail** → `_sass/_variables.scss` first (defines palette), then specific partials.
**Refresh citations manually** → push a commit to `main` (triggers `page_build`); or wait for the 08:00 UTC cron. Verify the JSON landed on the `google-scholar-stats` branch.
**Set up citations on a fresh fork** → add the `GOOGLE_SCHOLAR_ID` repo secret and enable Actions.

## Things to avoid

- Don't commit `_site/` — gitignored.
- Don't edit `Gemfile.lock` by hand; `bundle update <gem>` to modify.
- The `google-scholar-stats` branch is overwritten by the workflow on every run — don't base feature branches on it.
- `compress_html` is configured to skip compression in `development` env only, so production HTML is minified.