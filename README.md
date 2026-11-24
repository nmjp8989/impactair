# IMPACTAIR

The default IMPACTAIR website, based on the supplied eleven-page mobile design package. About Us matches the separately supplied desktop reference’s content, photography, body typography and cards, while keeping the existing site logo and navigation unchanged. Its top hero and closing call to action span the full page width; the responsive middle content is capped at 1440 px. The About page ends with its closing call to action and does not render a footer.

## Publishing

GitHub Pages serves the repository’s `main` branch at `/` (root). `index.html` is the default homepage. All pages, styles, scripts, fonts and images are local static files; no package installation or server runtime is required.

## Pages

The primary experience contains Home, About Us, Benefits, Festivals & Events, 2027 Festival Opportunities, Festival Categories, Contact Us, Careers, Privacy Policy, Terms of Use and Artwork Specifications. Existing resource URLs are retained, including the gallery and its filters, rental options, case studies, agency information and FAQ.

## Editing

- `scripts/main_pages.py`: primary-page content, with About Us overridden by its dedicated reference module.
- `scripts/about_reference.py`: the exact About Us reference copy, statistics and page structure.
- `scripts/support_pages.py`: contact, careers, privacy, terms and artwork content.
- `scripts/build_site.py`: common accessible header, footer, metadata and static HTML generation.
- `assets/impactair.css` and `assets/impactair.js`: the current design and interactions.
- `assets/about-reference.css`: the active reference-matched About body, with styles scoped to that page’s content so they do not alter the shared logo, header or navigation.
- `assets/site.css`, `assets/site.js` and `assets/legacy-theme.css`: retained resources and their matching theme.

After changing content or shared templates, run `python scripts/build_site.py` and commit the generated HTML along with the source changes. The generator versions shared CSS/JavaScript URLs, the About stylesheet and About HTML navigation links so updated content does not reuse stale cached styling or page responses. The command also prepares an ignored `dist/` directory for local preview; GitHub Pages uses the root HTML files. Rebuilding requires only Python’s standard library. There is no required build step on deployment.

## Images and type

The attachment’s small mobile previews are design references, not embedded website pages. Text, navigation and controls are live HTML; icons and the favicon are SVG. A compact, locally hosted display font keeps headings sharp at any zoom level. Its license is in `assets/fonts/`.

Production hero and festival art are larger original assets matching the supplied visual direction. Avoid enlarging thumbnails or resaving images at low quality. All image elements have intrinsic dimensions, descriptive alternate text where needed, and deferred loading below the first screen.

The original About Us artwork is preserved in `assets/source/about-reference.png` and delivered through the pixel-identical, lossless `assets/about-reference.webp`. CSS selects its photographic regions while the exact supplied text and statistics remain live HTML. Dedicated local body fonts and SVG icons reproduce the reference treatment without changing the shared header. The middle `.about-ref-content` container has a 1440 px maximum width and adapts for mobile; the hero and closing call to action remain outside that cap. See `assets/ASSETS.md` for provenance and delivery details.

## Enquiries and content

The quote form prepares an email draft to the existing `info@impactair.ca` address. The visitor reviews and sends the draft in their email application; the website does not claim to submit messages to a backend. Festival enquiry links prefill the relevant campaign topic. No analytics, advertising cookies or external font service are included.

The ZIP describes its contact information and event dates as illustrative. The other pages omit placeholder telephone numbers and unconfirmed festival dates; the 2027 pages invite proposals with current availability rather than treating the ZIP’s sample event list or audience totals as verified data.

At the user’s explicit request, About Us reproduces the separately supplied desktop reference’s copy and statistics: **50 Festivals**, **7 Million People**, and **June–September 2027**. These figures come directly from that reference; they were not independently verified as part of the website implementation.

Careers describe expressions of interest rather than confirmed vacancies. Artwork dimensions from the design are marked as layout references requiring the final production template. Existing case-study concepts remain identified as concepts.
