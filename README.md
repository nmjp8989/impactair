# IMPACTAIR

The default IMPACTAIR website, based on the supplied eleven-page mobile design package. The site uses the reference’s navy, cyan and orange branding, bold italic headings and festival imagery, with responsive desktop and mobile layouts.

## Publishing

GitHub Pages serves the repository’s `main` branch at `/` (root). `index.html` is the default homepage. All pages, styles, scripts, fonts and images are local static files; no package installation or server runtime is required.

## Pages

The primary experience contains Home, About Us, Benefits, Festivals & Events, 2027 Festival Opportunities, Festival Categories, Contact Us, Careers, Privacy Policy, Terms of Use and Artwork Specifications. Existing resource URLs are retained, including the gallery and its filters, rental options, case studies, agency information and FAQ.

## Editing

- `scripts/main_pages.py`: primary-page content.
- `scripts/support_pages.py`: contact, careers, privacy, terms and artwork content.
- `scripts/build_site.py`: common accessible header, footer, metadata and static HTML generation.
- `assets/impactair.css` and `assets/impactair.js`: the current design and interactions.
- `assets/site.css`, `assets/site.js` and `assets/legacy-theme.css`: retained resources and their matching theme.

After changing content or shared templates, run `python scripts/build_site.py` and commit the generated HTML along with the source changes. The command also prepares an ignored `dist/` directory for local preview; GitHub Pages uses the root HTML files. Rebuilding requires only Python’s standard library. There is no required build step on deployment.

## Images and type

The attachment’s small mobile previews are design references, not embedded website pages. Text, navigation and controls are live HTML; icons and the favicon are SVG. A compact, locally hosted display font keeps headings sharp at any zoom level. Its license is in `assets/fonts/`.

Production hero and festival art are larger original assets matching the supplied visual direction. Avoid enlarging thumbnails or resaving images at low quality. All image elements have intrinsic dimensions, descriptive alternate text where needed, and deferred loading below the first screen.

## Enquiries and content

The quote form prepares an email draft to the existing `info@impactair.ca` address. The visitor reviews and sends the draft in their email application; the website does not claim to submit messages to a backend. Festival enquiry links prefill the relevant campaign topic. No analytics, advertising cookies or external font service are included.

The ZIP describes its contact information and event dates as illustrative. Placeholder telephone numbers, unconfirmed festival dates and unsupported audience totals are not published as facts. The 2027 pages invite proposals with current availability. Careers describe expressions of interest rather than confirmed vacancies. Artwork dimensions from the design are marked as layout references requiring the final production template. Existing case-study concepts remain identified as concepts.
