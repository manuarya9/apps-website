# Vedyn Apps — SEO Action Plan

Goal: rank at the top of search for the jobs our apps do ("highlight cursor mac",
"hide desktop icons before screen sharing"), before and independent of App Store ranking.
Context: per `cloak/docs/strategy_review_2026-06.md`, distribution — not product — is the
current risk; CleanSlate is out-marketing Cloak on content. This plan closes that gap.

## Done in this branch (technical SEO baseline)

- [x] Canonical URLs on every page
- [x] Open Graph + Twitter Card meta on every page
- [x] JSON-LD: `Organization` + `WebSite` (home), `SoftwareApplication` (ShowPoint, Cloak, LumaSip), `FAQPage` (ShowPoint, Cloak)
- [x] `robots.txt` (excludes `/docs/` and legacy `/periodtracker/`) + `sitemap.xml`
- [x] Keyword-targeted `<title>`/meta descriptions on ShowPoint and Cloak pages
- [x] On-page FAQ sections targeting long-tail queries on ShowPoint and Cloak pages

## Next actions (prioritized)

### P0 — the moment App Store listings go live
1. Replace `href="#"` CTA placeholders on `/showpoint/` and `/cloak/` with real
   `https://apps.apple.com/app/id…` links. Search engines treat dead CTAs as low quality;
   users bounce.
2. Add each app's App Store URL to its `SoftwareApplication` JSON-LD as `"installUrl"`
   and `"sameAs"`.
3. Register the site in Google Search Console + Bing Webmaster Tools; submit `sitemap.xml`.

### P1 — within 2 weeks of launch
4. **Proper OG images** (1200×630) per app — current fallback is the 1024 brand mark.
   Render from app screenshots (`cursoroverlay/docs/app-store-screenshots/` already has
   1280×800 assets to crop). Social shares with real product imagery convert far better.
5. **Comparison pages** (the highest-intent commercial keywords):
   - `/showpoint/vs/` — ShowPoint vs Mouzz vs Cursor Pro vs Presentify (honest feature/price
     table; we win on lifetime pricing, no screen-recording permission, polish)
   - `/cloak/vs/` — Cloak vs Stealthly vs CleanSlate vs DeskMat (we win on $6.99 one-time
     vs $12.99/subscription, crash-safe restore, zero-permission free tier)
6. **How-to articles** (informational keywords that funnel to the product):
   - "How to highlight your cursor in a screen recording on Mac" → ShowPoint
   - "How to show mouse clicks on screen on macOS" → ShowPoint
   - "How to hide desktop icons on Mac (one keystroke)" → Cloak
   - "How to silence notifications while screen sharing on Mac" → Cloak
   Each: ~800–1200 words, answer the question fully (including the manual/Terminal way),
   then position the app as the one-keystroke path. Use `HowTo` or `Article` JSON-LD.

### P2 — ongoing
7. Launch posts: Product Hunt, Hacker News (Show HN), relevant subreddits
   (r/macapps, r/MacOS), MacMenuBar.com, AlternativeTo listings — these are the backlinks
   that move domain authority for indie Mac apps.
8. Rotate App Store promotional text with each release (see `app-store-optimization` skill);
   mirror seasonal messaging on the web pages.
9. Cross-link sibling apps ("Also from Vedyn: Cloak — clean your desktop before you share")
   on each app page footer.
10. Watch Search Console queries monthly; add FAQ entries for queries we rank #5–#15 on.

## Keyword targets

| Page | Primary | Secondary |
|------|---------|-----------|
| /showpoint/ | cursor highlighter mac | highlight mouse clicks screen recording, spotlight cursor presentation mac, show clicks in zoom |
| /cloak/ | hide desktop icons mac | clean desktop screen sharing, mute notifications screen share mac, presentation mode mac |
| Home | vedyn apps | privacy-first mac apps, one-time purchase mac utilities |

## Measurement

- Google Search Console: impressions/clicks per query, weekly after launch.
- Target: page-1 ranking for both primary keywords within 90 days of launch
  (low-competition long-tail; achievable with the comparison + how-to content above).
