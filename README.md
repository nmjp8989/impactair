# IMPACTAIR

Static, responsive website implementing the eleven supplied desktop page designs: Home, About Us, Benefits, Why Festivals, 2027 Festival Opportunities, Festival Categories, Contact Us, Careers, Privacy Policy, Terms of Use and Artwork Specifications. Headings, copy, controls and diagrams are HTML/SVG; CSS selects photographic regions from the original reference artwork.

All **19 routes** share the same logo and navigation, including the Solutions, Festivals and More dropdowns. The eight retained resource routes are `advertising-solutions.html`, `billboard-specifications.html`, `case-studies.html`, `faq.html`, `festivals-events.html`, `for-advertising-agencies.html`, `gallery.html` and `rental-options.html`. Their existing content and interactions, including gallery filtering and previews, remain available.

## Build and publish

```sh
python scripts/build_site.py
```

The generator requires only Python's standard library. It writes the eleven reference pages, refreshes the shared header/footer on the eight retained routes, versions stylesheet/script URLs, and copies the site into an ignored `dist/` directory for preview. Commit the source changes and generated root HTML together.

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
| `assets/reference-pages.css` | Shared reference styling and consistent navigation across all routes |
| `assets/*-reference.css` | Page-specific reference layouts and responsive reflow |
| `assets/impactair.css`, `assets/impactair.js` | Base styling, navigation and enquiry behavior for the eleven generated pages |
| `assets/site.css`, `assets/site.js`, `assets/legacy-theme.css` | Retained resource styling and behavior |

`scripts/main_pages.py` and `scripts/support_pages.py` retain the earlier base definitions; the reference modules override their page content in the build. Edit the active reference module for these eleven pages.

## Artwork and responsive behavior

The eleven 1024 × 1536 source PNGs in `assets/references/` are unchanged copies of the supplied designs. They are used as photographic source sheets, not flattened complete webpages. Native text, SVG icons and vector measurement diagrams stay sharp at browser zoom; photographic detail remains limited to the pixels in the supplied artwork. No higher-resolution photo source is implied by displaying a crop at a larger size. See `assets/ASSETS.md` for provenance and URL/cropping conventions.

The approved About body is preserved, including its full-width hero and closing call to action, 1440 px middle-content cap, mobile reflow, local fonts and pixel-identical lossless WebP source. It uses the same shared header as the other routes.

## Enquiries and supplied content

The contact form validates the required fields and opens an email draft to `info@impactair.ca`. The visitor reviews and sends it in their email application; there is no form-submission backend. Festival links prefill the selected topic. Careers and artwork submission also use email links. The mockup's fixture phone number and unprovided social-profile links are omitted. Request Full Festival List opens a relevant enquiry rather than presenting an invented event schedule.

The **50 Festivals**, **7 Million People** and **June–September 2027** campaign figures, featured event names and policy copy come from the supplied designs. They were not independently verified as part of implementation. No analytics, advertising cookies or external font service are included.

The large billboard is consistently described as **40 ft × 22 ft**, following the Artwork Specifications reference and resolving the Benefits mockup's conflicting 40 ft × 20 ft label. The second format is **20 ft × 20 ft**. Their respective safe areas are **35.43 ft × 15.74 ft** and **17.72 ft × 14.31 ft**; the page presents these dimensions as native text and SVG.
