# IMPACTAIR

Static, responsive website implementing twelve supplied desktop page designs: Home, About Us, Benefits, Why Festivals, 2027 Festival Opportunities, Festival Categories, Contact Us, Careers, Privacy Policy, Terms of Use, Artwork Specifications and For Advertising Agencies. Headings, copy, controls and diagrams are HTML/SVG; CSS selects photographic regions from the original reference artwork.

All **17 routes** share the same logo and navigation, including the Solutions, Festivals and More dropdowns. The five retained resource routes are `advertising-solutions.html`, `billboard-specifications.html`, `faq.html`, `festivals-events.html` and `gallery.html`. Their existing content and interactions, including gallery filtering and previews, remain available.

The simplified main navigation is Home, About, Solutions, Festivals, More and Request a Quote. Solutions contains Benefits, Artwork Specifications and For Advertising Agencies; Festivals contains Why Festivals and Festival Categories. Advertising Solutions, Billboard Specifications, 2027 Festival Opportunities and Gallery retain their direct URLs but are omitted from the navigation. The Rentals and Case Studies pages have been removed.

Every route also has the same bottom navigation: **About, Careers, Contact, FAQ, Privacy Policy and Terms of Use**, in that order. One shared footer is rendered after each page's main content, including About; page-specific closing call-to-action sections remain intact.

## Build and publish

```sh
python scripts/build_site.py
```

The generator requires only Python's standard library. It writes the twelve reference pages, refreshes the shared header/footer on the five retained routes, versions stylesheet/script URLs, and copies the site into an ignored `dist/` directory for preview, removing stale HTML outputs. Commit the source changes and generated root HTML together.

GitHub Pages serves the repository's `main` branch from `/` (root), with `index.html` as the homepage, at https://nmjp8989.github.io/impactair/. Deployment needs no package installation, application server or additional build step.

## Source map

| Source | Responsibility |
| --- | --- |
| `scripts/build_site.py` | Shared navigation, footer, metadata, asset versioning and generation |
| `scripts/design_common.py` | Reference photo crops, heroes, buttons, statistics and ribbons |
| `scripts/home_benefits_reference.py` | Home and Benefits |
| `scripts/about_reference.py` | Preserved approved About composition and copy |
| `scripts/festival_reference.py` | Why Festivals, 2027 Opportunities and Festival Categories |
| `scripts/support_reference.py` | Contact, Careers, Privacy, Terms and Artwork Specifications |
| `scripts/agency_reference.py`, `assets/agency-reference.css` | For Advertising Agencies reference content and layout |
| `assets/reference-pages.css` | Shared reference styling and consistent header/footer navigation across all routes |
| `assets/*-reference.css` | Page-specific reference layouts and responsive reflow |
| `assets/impactair.css`, `assets/impactair.js` | Base styling, navigation and enquiry behavior for the twelve generated pages |
| `assets/site.css`, `assets/site.js`, `assets/legacy-theme.css` | Retained resource styling and behavior |

`scripts/main_pages.py` and `scripts/support_pages.py` retain the earlier base definitions; the reference modules provide the active page content in the build. Edit the appropriate reference module for these twelve pages.

## Artwork and responsive behavior

The twelve 1024 × 1536 source PNGs in `assets/references/`, including `agencies.png`, are unchanged copies of the supplied designs. They are used as photographic source sheets, not flattened complete webpages. Native text, SVG icons and vector measurement diagrams stay sharp at browser zoom; photographic detail remains limited to the pixels in the supplied artwork. No higher-resolution photo source is implied by displaying a crop at a larger size. See `assets/ASSETS.md` for provenance and URL/cropping conventions.

The approved About body is preserved, including its full-width hero and closing call to action, 1440 px middle-content cap, mobile reflow, local fonts and pixel-identical lossless WebP source. It uses the same shared header as the other routes. The shared bottom navigation is appended after that body at the user's request.

## Enquiries and supplied content

The contact form validates the required fields and opens an email draft to `info@impactair.ca`. The visitor reviews and sends it in their email application; there is no form-submission backend. Festival links prefill the selected topic. Careers and artwork submission also use email links. The mockup's fixture phone number and unprovided social-profile links are omitted. Request Full Festival List opens a relevant enquiry rather than presenting an invented event schedule.

The **50 Festivals**, **7 Million People** and **June–September 2027** campaign figures, featured event names and policy copy come from the supplied designs. They were not independently verified as part of implementation. No analytics, advertising cookies or external font service are included.

The large billboard is consistently described as **40 ft × 22 ft**, following the Artwork Specifications reference and resolving the Benefits mockup's conflicting 40 ft × 20 ft label. The second format is **20 ft × 20 ft**. Their respective safe areas are **35.43 ft × 15.74 ft** and **17.72 ft × 14.31 ft**; the page presents these dimensions as native text and SVG.
