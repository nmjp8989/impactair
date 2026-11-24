# Production artwork

The eleven mobile PNGs in the supplied ZIP are visual design references. They include phone frames and are not used as flattened webpage images.

## User-supplied About Us desktop reference

The user subsequently supplied a separate desktop About Us design and requested that its artwork, layout and copy be reproduced exactly. It is preserved separately from the generated promotional assets below.

| Source | Native dimensions | Website delivery |
| --- | --- | --- |
| `source/about-reference.png` | 1024 × 1536 | `about-reference.webp` — lossless WebP at the original dimensions |

The PNG is an unchanged copy of the supplied artwork. The WebP preserves its pixels without lossy recompression. `about-reference.css` displays the Who We Are and closing-banner photographic regions from that asset. The user subsequently requested a full-width top banner consistent with Home; About therefore uses the shared header and homepage hero component with the larger `hero-festival.webp` responsive image set. The complete screenshot is not used as a flattened functional page. Headings, body copy, statistics, buttons and icons are recreated as native HTML/SVG, and the responsive mobile layout stacks the sections while retaining the supplied visual identity.

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

Existing `design-*` and other historical assets remain available to the retained resource pages. Shared icons and the favicon are SVG. `about-icons.svg` supplies the thinner outline symbols used by the desktop About reference. The main display font is a local Latin subset of DejaVu Sans Condensed Bold Oblique. About uses additional local subsets of DejaVu Sans Bold Oblique (`about-display.woff`) and DejaVu Sans Condensed Bold (`about-headings.woff`) for its wider italic titles and heavier section headings. Their license is included in `fonts/DejaVu-LICENSE.txt`. Typography, controls and branding remain live/vector elements, preserving clarity at browser zoom and on high-density displays.
