# Artwork provenance and delivery

## Current supplied references

All twelve files below are **unchanged 1024 × 1536 PNG copies** of the user's supplied desktop designs. Their contents are preserved at the original resolution.

| File in `assets/references/` | Supplied design |
| --- | --- |
| `home.png` | Home |
| `about.png` | About Us |
| `benefits.png` | Benefits |
| `festivals.png` | Why Festivals |
| `opportunities.png` | 2027 Festival Opportunities |
| `categories.png` | Festival Categories |
| `contact.png` | Contact Us |
| `careers.png` | Careers |
| `privacy.png` | Privacy Policy |
| `terms.png` | Terms of Use |
| `artwork.png` | Artwork Specifications |
| `agencies.png` | For Advertising Agencies |

The website reconstructs the supplied layouts using HTML, CSS and SVG. Source sheets supply photographic regions through clipped image elements or masked CSS backgrounds. Page headings, body copy, statistics, form controls, navigation, buttons, icons and technical dimensions remain live text/vector content. The Privacy and Terms bodies use native text; the artwork diagrams are in `artwork-diagrams.svg`. `scripts/agency_reference.py` and `assets/agency-reference.css` implement the additional For Advertising Agencies design using the unchanged `references/agencies.png` source.

CSS cropping does not create new image detail. These photographs have the resolution present in the supplied 1024 px-wide sheets; displaying them larger can soften them. No generated replacement or invented higher-resolution master is claimed for the current reference implementation. Keep the original files unchanged, avoid lossy resaves, and use native text/SVG for editable labels.

### Crop and URL conventions

`scripts/design_common.py` supplies common crop helpers; `scripts/support_reference.py` supplies the supporting-page equivalents. Photo elements preserve the source aspect ratio, use `max-width: none` and select the required region with offsets/transforms. Background masks suppress the reference's original interface text while revealing its scenery.

An ordinary HTML image uses `src="assets/references/home.png"`. A URL custom property consumed by a stylesheet inside `assets/` uses `url('references/home.png')`. Retain this distinction: `url('assets/references/home.png')` in that background custom property resolves to an incorrect doubled `assets/assets/` path. Verify background rendering in a browser after changing crop helpers; a file-existence scan alone does not establish CSS URL behavior.

## Preserved approved About artwork

About retains its separately approved implementation:

| Source | Delivery |
| --- | --- |
| `source/about-reference.png` — 1024 × 1536 | `about-reference.webp` — pixel-identical lossless WebP |

`about-reference.css` selects its photographic regions. `scripts/about_reference.py` supplies the exact requested copy, statistics and structure; `about-icons.svg`, `fonts/about-display.woff` and `fonts/about-headings.woff` supply the body icons and typography. The hero and closing call to action span the page width; the middle content is capped at 1440 px and reflows on mobile. This approved body is preserved, with the site's shared footer appended after it at the user's request.

## Existing promotional and historical assets

Earlier generated promotional concepts remain available for retained resource pages and social-sharing metadata. They illustrate campaign settings, not confirmed festival participation, and are not higher-resolution copies of the new references.

| Earlier master in `assets/source/` | Native size | Existing delivery |
| --- | --- | --- |
| `hero-festival.png` | 1672 × 941 | `hero-festival.webp` and 768/1280-width variants |
| `festival-music.png` | 1536 × 1024 | `festival-music.webp` and 768/1280-width variants |
| `festival-food.png` | 1536 × 1024 | `festival-food.webp` and 768/1280-width variants |
| `festival-culture.png` | 1536 × 1024 | `festival-culture.webp` and 768/1280-width variants |
| `festival-community.png` | 1536 × 1024 | `festival-community.webp` and 768/1280-width variants |

Historical `design-*` and other assets remain for existing resources. Some contain an older red-logo treatment; they are not the visual source for the current navy/cyan/orange reference pages. The older mobile thumbnails are design records, not large-image sources.

## Vector assets, typography and content attribution

The shared wordmark is native text/CSS. `icons.svg`, `reference-icons.svg`, `about-icons.svg`, inline SVG and `artwork-diagrams.svg` keep interface and measurement graphics scalable. Fonts are hosted locally; their license is in `fonts/DejaVu-LICENSE.txt`.

All 17 routes use the same native bottom-navigation links: About, Careers, Contact, FAQ, Privacy Policy and Terms of Use. The footer is generated once per page by `scripts/build_site.py`; original reference artwork is not altered to change the navigation.

Campaign statistics and event names reproduce the supplied copy and are not independently verified audience or schedule data. Technical dimensions follow the Artwork Specifications reference: 40 ft × 22 ft with a 35.43 ft × 15.74 ft safe area, and 20 ft × 20 ft with a 17.72 ft × 14.31 ft safe area. Benefits uses the same 40 ft × 22 ft overall dimensions for consistency.
