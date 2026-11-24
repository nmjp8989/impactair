"""User-supplied About Us copy presented in the shared IMPACTAIR design."""

from main_pages import icon, image


ABOUT_REFERENCE = {
    "title": "About Us",
    "description": "IMPACTAIR specializes in high-impact inflatable billboard rentals that give brands unmatched visibility at Ontario’s largest festivals, events and public gatherings.",
    "hero": "home",
    "heading": "ABOUT <em>US</em>",
    "kicker": "Inflatable billboard advertising",
    "intro": "Ontario’s Leader in Inflatable Billboard Advertising for Major Events.",
    "actions": [("Request a Quote", "contact.html#quote", ""), ("Contact Us", "contact.html", "button-outline")],
    "body": f'''
<section class="section">
  <div class="wrap split-section">
    <div class="section-copy">
      <h2>Who We Are</h2>
      <p><strong>IMPACTAIR</strong> specializes in high-impact inflatable billboard rentals that give brands unmatched visibility at Ontario’s largest festivals, events and public gatherings.</p>
      <p>We combine oversized, eye-catching advertising with strategic event placements to help businesses, brands and organizations reach massive, live audiences across the GTA and beyond.</p>
    </div>
    <figure class="feature-photo">{image('festival-community.webp', 'Festival visitors and white tents in an Ontario park with the Toronto skyline in the background')}</figure>
  </div>
</section>

<section class="section section-tint" aria-label="Our mission, vision and values">
  <div class="wrap card-grid three-columns">
    <article class="info-card">
      {icon('target')}
      <h3>Our Mission</h3>
      <p>To deliver bold, innovative and high-visibility advertising solutions that create real audience impact for our clients.</p>
    </article>
    <article class="info-card">
      {icon('eye')}
      <h3>Our Vision</h3>
      <p>To be Canada’s most trusted event advertising partner, bringing brands closer to millions of people through standout outdoor media.</p>
    </article>
    <article class="info-card">
      {icon('handshake')}
      <h3>Our Values</h3>
      <p><strong>Impact</strong> – Maximum visibility</p>
      <p><strong>Reliability</strong> – Professional, on-time service</p>
      <p><strong>Partnership</strong> – Your success is our priority</p>
      <p><strong>Innovation</strong> – Creative, larger-than-life solutions</p>
    </article>
  </div>
</section>

<section class="planning-strip" aria-label="Festival audience and season">
  <div class="wrap planning-grid">
    <div>{icon('calendar')}<p><strong>50</strong><span>Festivals</span></p></div>
    <div>{icon('users')}<p><strong>7 Million</strong><span>People</span></p></div>
    <div>{icon('calendar')}<p><span>June–September</span><strong>2027</strong></p></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-heading">
      <h2>Why Choose <em>IMPACTAIR?</em></h2>
      <p>We turn event spaces into powerful branding opportunities with large-scale inflatable billboards that command attention, drive engagement and leave a lasting impression.</p>
    </div>
    <div class="benefit-grid">
      <article class="benefit-card">{icon('users')}<div><h3>Massive Audience Reach</h3></div></article>
      <article class="benefit-card">{icon('eye')}<div><h3>High-Impact Brand Exposure</h3></div></article>
      <article class="benefit-card">{icon('pin')}<div><h3>Prime Event Locations</h3></div></article>
      <article class="benefit-card">{icon('plug')}<div><h3>Full Service Support</h3></div></article>
      <article class="benefit-card">{icon('layers')}<div><h3>Flexible Rental Options</h3></div></article>
    </div>
  </div>
</section>

<section class="section cta-section">
  <div class="wrap campaign-cta">
    <div class="cta-image">{image('hero-festival.webp', '')}</div>
    <div class="cta-copy">
      <h2>LET’S MAKE<br><em>YOUR BRAND UNMISSABLE.</em></h2>
      <div class="hero-actions">
        <a class="button" href="contact.html#quote">Request a Quote</a>
        <a class="button button-outline" href="contact.html">Contact Us</a>
      </div>
    </div>
  </div>
</section>
''',
}
