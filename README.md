# apps-website

Static website for all manuarya9 apps. Hosted on Cloudflare Pages.

## Apps

| App | Folder | Status |
|-----|--------|--------|
| [ShowPoint](showpoint/) | `/showpoint` | macOS, menu-bar cursor overlay |
| [LumaSip](lumasip/) | `/lumasip` | iOS, water tracker |
| [Period Tracker](periodtracker/) | `/periodtracker` | iOS, coming soon |

## Updating an app page

Edit the relevant `index.html` directly:

- `showpoint/index.html` — App Store link, features, pricing
- `lumasip/index.html` — App Store link, features
- `periodtracker/index.html` — Launch date, features

Push to `main` and Cloudflare Pages auto-deploys within ~60 seconds.

## Adding a new app

1. Create a new folder: `mkdir newapp`
2. Copy an existing `index.html` into it and update the content
3. Add a card to `index.html` in the root
4. Push to `main`

## Structure

```
apps-website/
├── index.html          ← landing page (all apps)
├── showpoint/
│   └── index.html      ← ShowPoint app page
├── lumasip/
│   └── index.html      ← LumaSip app page
├── periodtracker/
│   └── index.html      ← Period Tracker app page
├── assets/
│   └── style.css       ← shared styles
├── _headers            ← Cloudflare security headers
└── _redirects          ← Cloudflare redirect rules
```
