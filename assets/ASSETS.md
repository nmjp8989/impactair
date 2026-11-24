# Production artwork

The eleven mobile PNGs in the supplied ZIP are visual design references. They include phone frames and are not used as flattened webpage images.

## User-supplied About Us desktop reference

The About Us page matches the user-supplied desktop reference’s photography, exact copy, body typography, cards and section composition. The existing shared site logo and navigation remain unchanged. The original reference is preserved separately from the generated promotional assets below.

| Source | Native dimensions | Website delivery |
| --- | --- | --- |
| `source/about-reference.png` | 1024 × 1536 | `about-reference.webp` — lossless WebP at the original dimensions |

The PNG is an unchanged copy of the supplied artwork. The lossless WebP is pixel-identical to that source and is used by `about-reference.css` as a source sheet for the photographic regions. Headings, body copy, statistics, buttons and icons are native HTML/SVG, not flattened screenshot text. The page uses the dedicated local `about-display.woff` and `about-headings.woff` body fonts and `about-icons.svg` to reproduce the reference treatment.

The About stylesheet is scoped to the page content and does not override the shared logo, header or navigation. The top hero and closing call to action span the full page width. Between them, `.about-ref-content` caps the middle sections at 1440 px and rearranges them for mobile. The page ends at the closing call to action, with no footer. The generator versions the About stylesheet URL and About HTML navigation links to avoid serving the prior layout from cache.

`scripts/about_reference.py` contains the exact requested copy, including **50 Festivals**, **7 Million People**, and **June–September 2027**. These are user-requested statements from the desktop reference, not independently verified event or audience data. This separate reference does not change the original ZIP’s notice that its sample contact information and festival dates are illustrative.

## New image masters

The following promotional concept images were created with the built-in image generation tool to provide larger, clean artwork in the supplied navy/cyan/orange visual style. They illustrate campaign settings and do not document confirmed festival participation.

| Master | Native dimensions | Website delivery |
| --- | --- | --- |
| `source/hero-festival.png` | 1672 × 941 | `hero-festival.webp` and 768/1280-width variants |
| `source/festival-music.png` | 1536 × 1024 | `festival-music.webp` and 768/1280-width variants |
| `source/festival-food.png` | 1536 × 1024 | `festival-food.webp` and 768/1280-width variants |
| `source/festival-culture.png` | 1536 × 1024 | `festival-culture.webp` and 768/1280-width variants |
| `source/festival-community.png` | 1536 × 1024 | `festival-community.webp` and 768/1280-width variants |

WebP delivery files use quality 94 encoding. Smaller variants are downsampled from the native master; no image has been artificially enlarged. The HTML `sizes` hints account for cover-cropping so high-density displays select sufficient source pixels. Images below the first screen are lazy-loaded. Native dimensions reserve layout space.

The PNG masters total 14,814,489 bytes; the five full-size WebP delivery images total 2,950,600 bytes. Responsive variants can reduce transfer further. PNG masters are retained for future editing and are not loaded by the website.

## Generation briefs

**Hero:** Production website hero background inspired by the supplied ImpactAir phone mockups, using scenery and billboard style only. Landscape Toronto CN Tower skyline at blue/pink sunset, white festival tents, warm string lights and a lively crowd. Upright navy inflatable billboard on the right, small white/cyan IMPACTAIR branding, exact white “YOUR / BRAND / HERE” lettering and an orange swoosh. Open dark-blue sky at left for live HTML text. Crisp photographic advertising concept; no phone frame, interface, buttons, watermark or text outside the billboard.

**Music:** High-resolution landscape promotional concert scene with purple, cyan and golden stage lights, an enthusiastic outdoor crowd, dusk skyline and CN Tower. Crisp stage and crowd detail. No interface, overlaid words, watermark or logos.

**Food:** High-resolution landscape food festival with white tents, food stalls, warm string lights and diverse visitors, in a sunset Toronto setting. Detailed natural promotional concept imagery; no interface, overlaid words, watermark or logos.

**Culture:** High-resolution landscape Caribbean carnival scene with adult performers in turquoise, red, yellow and gold feathered costumes, in a bright daytime festival setting. Detailed natural promotional concept imagery; no interface, overlaid words, watermark or logos.

**Community:** High-resolution landscape community festival with families and friends, white tents in a green Ontario park, blue sky and Toronto skyline. Detailed natural promotional concept imagery; no interface, overlaid words, watermark or logos.

## Other assets

Existing `design-*` and other historical assets remain available to the retained resource pages. Shared icons and the favicon are SVG. The shared site design uses the local Latin subset of DejaVu Sans Condensed Bold Oblique in `impact-display.woff`. About uses that shared header unchanged and loads `about-icons.svg`, `about-display.woff` and `about-headings.woff` for its reference-matched body. The font license is included in `fonts/DejaVu-LICENSE.txt`. Typography, controls and branding remain live/vector elements, preserving clarity at browser zoom and on high-density displays.
