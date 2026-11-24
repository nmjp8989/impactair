"""About Us content transcribed from the supplied desktop reference.

The background artwork is supplied through about-reference.css. Text, icons
and navigation remain native page elements for clear rendering and access.
"""


def icon(name):
    return (f'<svg class="about-ref-icon" aria-hidden="true" width="64" height="64">'
            f'<use href="assets/about-icons.svg#{name}"></use></svg>')


BINOCULARS = '''<svg class="about-ref-icon" aria-hidden="true" width="64" height="64" viewBox="0 0 64 64">
  <g fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="16" cy="43" r="12"/><circle cx="48" cy="43" r="12"/>
    <path d="M5 38 14 17a5 5 0 0 1 9 0l5 20m31 1-9-21a5 5 0 0 0-9 0l-5 20M28 41h8M27 32a7 7 0 0 1 10 0"/>
  </g>
</svg>'''

GEAR = '''<svg class="about-ref-icon" aria-hidden="true" width="64" height="64" viewBox="0 0 32 32">
  <g fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
    <path d="M13 2h6l.8 4.1 2.2.9 3.5-2.3 4.2 4.2-2.3 3.5.9 2.2 4.1.8v6l-4.1.8-.9 2.2 2.3 3.5-4.2 4.2-3.5-2.3-2.2.9-.8 4.1h-6l-.8-4.1-2.2-.9-3.5 2.3-4.2-4.2 2.3-3.5-.9-2.2L-1 21.4v-6l4.1-.8.9-2.2-2.3-3.5 4.2-4.2 3.5 2.3 2.2-.9Z" transform="translate(3 1) scale(.8)"/>
    <circle cx="16" cy="15.7" r="4.5"/>
  </g>
</svg>'''

CHECK = '''<svg class="about-ref-check" aria-hidden="true" width="18" height="18" viewBox="0 0 24 24"><path d="m5 12 4 4 10-10" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''


ABOUT_REFERENCE = {
    "title": "About Us",
    "description": "IMPACTAIR specializes in high-impact inflatable billboard rentals that give brands unmatched visibility at Ontario’s largest festivals, events and public gatherings.",
    "custom_layout": True,
    "extra_css": "assets/about-reference.css",
    "no_footer": True,
    "heading": "ABOUT <em>US</em>",
    "kicker": "",
    "intro": "Ontario’s Leader in Inflatable Billboard Advertising for Major Events.",
    "body": f'''
<div class="about-reference-page">
  <svg width="0" height="0" aria-hidden="true" style="position:absolute"><defs><clipPath id="about-who-photo-clip" clipPathUnits="objectBoundingBox"><path d="M .216 0 H 1 V 1 H .027 C .009 1 -.004 .980 .002 .953 L .154 .080 C .170 .023 .184 0 .216 0 Z"/></clipPath></defs></svg>
  <section class="about-ref-hero">
    <div class="about-ref-hero-art" aria-hidden="true"></div>
    <div class="about-ref-wrap">
      <div class="about-ref-hero-copy">
        <h1>ABOUT <em>US</em></h1>
        <p>Ontario’s Leader in Inflatable<br>Billboard Advertising<br>for Major Events.</p>
      </div>
    </div>
  </section>

  <div class="about-ref-content">
  <section class="about-ref-who">
    <div class="about-ref-wrap">
      <div class="about-ref-who-copy">
        <h2>Who We Are</h2>
        <p><strong>IMPACTAIR</strong> specializes in high-impact inflatable billboard rentals that give brands unmatched visibility at Ontario’s largest festivals, events and public gatherings.</p>
        <p>We combine oversized, eye-catching<br class="about-ref-desktop-break"> advertising with strategic event placements<br class="about-ref-desktop-break"> to help businesses, brands and organizations<br class="about-ref-desktop-break"> reach massive, live audiences across the GTA<br class="about-ref-desktop-break"> and beyond.</p>
      </div>
      <div class="about-ref-who-art" role="img" aria-label="IMPACTAIR inflatable billboard with a red maple leaf and Toronto Events branding, above a festival crowd beside the Toronto skyline."></div>
    </div>
  </section>

  <section class="about-ref-principles" aria-label="Our mission, vision and values">
    <div class="about-ref-wrap">
      <article class="about-ref-principle about-ref-mission">
        {icon('target')}
        <div><h3>Our Mission</h3><p>To deliver bold, innovative and high-visibility advertising solutions that create real audience impact for our clients.</p></div>
      </article>
      <article class="about-ref-principle about-ref-vision">
        {BINOCULARS}
        <div><h3>Our Vision</h3><p>To be Canada’s most trusted<br class="about-ref-desktop-break"> event advertising partner, bringing<br class="about-ref-desktop-break"> brands closer to millions of people<br class="about-ref-desktop-break"> through standout outdoor media.</p></div>
      </article>
      <article class="about-ref-principle about-ref-values">
        {icon('handshake')}
        <div><h3>Our Values</h3><ul>
          <li>{CHECK}<span><strong>Impact</strong> – Maximum visibility</span></li>
          <li>{CHECK}<span><strong>Reliability</strong> – Professional, on-time service</span></li>
          <li>{CHECK}<span><strong>Partnership</strong> – Your success is our priority</span></li>
          <li>{CHECK}<span><strong>Innovation</strong> – Creative, larger-than-life solutions</span></li>
        </ul></div>
      </article>
    </div>
  </section>

  <section class="about-ref-stats" aria-label="Festival audience and season">
    <div class="about-ref-wrap">
      <div class="about-ref-stat about-ref-stat-festivals">
        {icon('calendar-empty')}<div><strong>50</strong><span>FESTIVALS</span></div>
      </div>
      <div class="about-ref-stat about-ref-stat-audience">
        {icon('users')}<div><strong>7 MILLION</strong><span>PEOPLE</span></div>
      </div>
      <div class="about-ref-stat about-ref-stat-season">
        {icon('calendar')}<div><span>JUNE – SEPTEMBER</span><strong>2027</strong></div>
      </div>
    </div>
  </section>

  <section class="about-ref-why">
    <div class="about-ref-wrap">
      <div class="about-ref-why-copy">
        <h2>Why Choose<br>IMPACTAIR?</h2>
        <p>We turn event spaces into powerful branding opportunities with large-scale inflatable billboards that command attention, drive engagement and leave a lasting impression.</p>
      </div>
      <div class="about-ref-reasons">
        <article class="about-ref-reason">{icon('users')}<h3>Massive<br>Audience<br>Reach</h3></article>
        <article class="about-ref-reason">{icon('eye')}<h3>High-Impact<br>Brand<br>Exposure</h3></article>
        <article class="about-ref-reason">{icon('pin')}<h3>Prime<br>Event<br>Locations</h3></article>
        <article class="about-ref-reason">{GEAR}<h3>Full<br>Service<br>Support</h3></article>
        <article class="about-ref-reason">{icon('layers')}<h3>Flexible<br>Rental<br>Options</h3></article>
      </div>
    </div>
  </section>

  </div>

  <section class="about-ref-cta">
    <div class="about-ref-cta-art" aria-hidden="true"></div>
    <div class="about-ref-wrap">
      <div class="about-ref-cta-copy">
        <h2>LET’S MAKE<br>YOUR BRAND UNMISSABLE.</h2>
        <div class="about-ref-cta-actions">
          <a class="button about-ref-quote" href="contact.html#quote">Request a Quote {icon('arrow-right')}</a>
          <a class="button button-outline about-ref-contact" href="contact.html">Contact Us</a>
        </div>
      </div>
    </div>
  </section>
</div>
''',
}
