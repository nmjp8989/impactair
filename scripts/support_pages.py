"""Supporting pages for the IMPACTAIR static website.

The reference artwork supplies page structure and visual direction. Contact
information comes from the existing site; unconfirmed production dimensions
are explicitly presented as references, not approved printing templates.
"""


def icon(name):
    return (f'<svg class="icon" aria-hidden="true" width="24" height="24">'
            f'<use href="assets/icons.svg#{name}"></use></svg>')


SUPPORT_PAGES = {
    "contact.html": {
        "title": "Contact Us & Request a Quote",
        "description": "Plan your next Ontario festival campaign with IMPACTAIR. Request an inflatable billboard quote or a 2027 media proposal.",
        "heading": "Contact <em>Us</em>",
        "kicker": "Let’s make an impact",
        "intro": "Let’s bring your brand to Ontario’s biggest festivals and events.",
        "body": f'''
<section class="section">
  <div class="wrap contact-grid">
    <div class="contact-methods">
      <h2 class="section-heading">Start a <em>conversation.</em></h2>
      <p>Tell us where you want to be seen. We’ll help you explore the right billboard, event and campaign options.</p>
      <div class="info-card">
        {icon("mail")}
        <div><h3>Email us</h3><a href="mailto:info@impactair.ca">info@impactair.ca</a></div>
      </div>
      <div class="info-card">
        {icon("pin")}
        <div><h3>Toronto (GTA) &amp; across Ontario</h3><p>Including Hamilton, Oakville, Burlington, Kitchener and surrounding areas.</p></div>
      </div>
      <div class="info-card">
        {icon("calendar")}
        <div><h3>Planning for 2027?</h3><p>Ask about festival opportunities, campaign timing and a proposal tailored to your brand.</p></div>
      </div>
    </div>
    <form class="quote-form" id="quote" action="mailto:info@impactair.ca" method="post" enctype="text/plain" data-email="info@impactair.ca">
      <h2>Send us a message</h2>
      <p class="form-note">Fields marked with an asterisk (*) are required.</p>
      <div class="form-grid">
        <label>Full name *<input name="name" autocomplete="name" maxlength="120" required></label>
        <label>Company / organization<input name="company" autocomplete="organization" maxlength="160"></label>
        <label>Email address *<input name="email" type="email" autocomplete="email" maxlength="254" required></label>
        <label>Phone number<input name="phone" type="tel" autocomplete="tel" maxlength="40"></label>
        <label class="field-wide">Preferred event date(s)<input name="dates" placeholder="e.g. Summer 2027" maxlength="160"></label>
        <label class="field-wide">Event / campaign details *<textarea name="project" rows="5" maxlength="4000" placeholder="Your event, location, audience and what you’d like to achieve…" required></textarea></label>
      </div>
      <p class="form-note">This opens a draft in your email app for you to review and send. You can also email <a href="mailto:info@impactair.ca">info@impactair.ca</a> directly.</p>
      <button class="button" type="submit">Prepare My Enquiry</button>
      <p class="form-note">Read our <a href="privacy-policy.html">Privacy Policy</a> for details about the enquiry form.</p>
      <p class="form-status" id="quote-status" role="status" aria-live="polite"></p>
      <noscript><p>Your email app can send the form, or you can email your event details directly.</p></noscript>
    </form>
  </div>
</section>''',
    },
    "careers.html": {
        "title": "Careers at IMPACTAIR",
        "description": "Share your interest in sales, creative work, event operations or marketing with the IMPACTAIR team.",
        "heading": "Careers at <em>ImpactAir</em>",
        "kicker": "Bring your talent",
        "intro": "Have talent? Drive sales? We want to hear from you.",
        "body": f'''
<section class="section">
  <div class="wrap">
    <div class="section-heading"><h2>Big ideas. <em>Real-world impact.</em></h2><p>Interested in helping brands stand out? Tell us where your experience could make a difference.</p></div>
    <div class="card-grid">
      <article class="info-card">{icon("target")}<h3>Sales Executives</h3><p>Build relationships with brands, agencies and event partners.</p></article>
      <article class="info-card">{icon("image")}<h3>Creative Talent</h3><p>Bring bold campaign ideas and memorable visual storytelling.</p></article>
      <article class="info-card">{icon("calendar")}<h3>Event Professionals</h3><p>Bring practical experience in planning, coordination and on-site delivery.</p></article>
      <article class="info-card">{icon("messages")}<h3>Marketing &amp; Promotions</h3><p>Connect campaigns with the audiences and communities they’re made for.</p></article>
    </div>
    <div class="info-card prose">
      <h2>Introduce yourself.</h2>
      <p>Email your résumé or portfolio, the area you’re interested in, and a little about what you bring to the team.</p>
      <p>We welcome expressions of interest. These areas describe the skills we’d like to hear about; they are not a list of confirmed vacancies.</p>
      <a class="button" href="mailto:info@impactair.ca?subject=IMPACTAIR%20career%20enquiry">Send Your Introduction</a>
    </div>
  </div>
</section>''',
    },
    "privacy-policy.html": {
        "title": "Privacy Policy",
        "description": "Learn how the IMPACTAIR website’s email enquiry form works and what information it uses.",
        "heading": "Privacy <em>Policy</em>",
        "kicker": "Your information",
        "intro": "How information is handled when you browse this website or prepare an enquiry.",
        "body": '''
<section class="section">
  <div class="wrap prose">
    <article class="info-card">
      <h2>Information you choose to share</h2>
      <p>The contact form lets you enter your name, company, email address, phone number, preferred dates and campaign details. Please include only information needed for your enquiry.</p>
      <h2>How the enquiry form works</h2>
      <p>The website prepares an email draft on your device. It does not send your enquiry to a website form service or save it in a website database. You review and send the draft using your own email application.</p>
      <p>When you send an email to <a href="mailto:info@impactair.ca">info@impactair.ca</a>, its contents are shared with IMPACTAIR so the team can respond to your enquiry. Your email provider also handles that message under its own terms and privacy practices.</p>
      <h2>Cookies and tracking</h2>
      <p>This website does not set advertising cookies or include an analytics or advertising-tracking service. Its navigation and enquiry form run in your browser.</p>
      <h2>Website hosting</h2>
      <p>The website’s hosting provider may process routine technical request information, such as IP addresses and browser details, to deliver the pages and operate its service. That processing is governed by the provider’s privacy practices.</p>
      <h2>Protecting your information</h2>
      <p>Please do not use the enquiry form to send payment-card information, identification documents or other sensitive personal information. Contact us first if your project requires a different way to share files.</p>
      <h2>Questions and updates</h2>
      <p>For questions about information you have emailed to IMPACTAIR, contact <a href="mailto:info@impactair.ca?subject=Privacy%20enquiry">info@impactair.ca</a>. This page will be updated if the website’s enquiry or tracking features change.</p>
    </article>
  </div>
</section>''',
    },
    "terms-of-use.html": {
        "title": "Terms of Use",
        "description": "Information about using the IMPACTAIR website, preparing enquiries and confirming campaign details.",
        "heading": "Terms of <em>Use</em>",
        "kicker": "Website information",
        "intro": "A few details to help you use our website and plan your campaign.",
        "body": '''
<section class="section">
  <div class="wrap prose">
    <article class="info-card">
      <h2>Using this website</h2>
      <p>This website introduces IMPACTAIR’s inflatable billboard advertising and provides a way to enquire about campaigns, events and creative requirements. Please use it responsibly and provide accurate contact details when making an enquiry.</p>
      <h2>Enquiries and bookings</h2>
      <p>Preparing or sending an enquiry does not reserve a billboard, confirm an event placement or create a booking. Available formats, locations, dates, pricing and delivery details must be confirmed directly with the IMPACTAIR team.</p>
      <h2>Festival and campaign information</h2>
      <p>Festival categories and campaign images illustrate possible advertising settings. Event participation, audience information and 2027 campaign availability should be confirmed in your proposal.</p>
      <h2>Artwork and brand assets</h2>
      <p>Submit only artwork and brand assets you are authorized to use. Request the production template for your confirmed billboard before preparing final print files. Illustrations and reference layouts on this website are not print-ready artwork.</p>
      <h2>Email and third-party services</h2>
      <p>Email links open your email application, which is provided by a separate service. Review the applicable provider’s terms and privacy information when using that service.</p>
      <h2>Updates and questions</h2>
      <p>Website information may change as campaign options develop. The written details agreed for your project govern that project. For questions about this website or a proposal, email <a href="mailto:info@impactair.ca">info@impactair.ca</a>.</p>
    </article>
  </div>
</section>''',
    },
    "artwork-specifications.html": {
        "title": "Artwork Specifications",
        "description": "Prepare clear, high-quality artwork for your IMPACTAIR inflatable billboard and request the production template for your campaign.",
        "heading": "Artwork <em>Specifications</em>",
        "kicker": "Designed to stand out",
        "intro": "Make every detail count. Start with the right template and crisp, production-ready artwork.",
        "body": f'''
<section class="section">
  <div class="wrap">
    <div class="section-heading"><h2>Start with your <em>production template.</em></h2><p>Ask our team for the template for your booked billboard. Confirm the print size, safe area, bleed, working scale, colour profile and required image resolution before exporting.</p></div>
    <div class="card-grid">
      <article class="info-card">{icon("image")}<h3>High-quality PDF</h3><p>Supply a print-ready PDF using the settings provided with your confirmed template. Embed all linked images.</p></article>
      <article class="info-card">{icon("layers")}<h3>Sharp type &amp; logos</h3><p>Use vector logos and outline text in the final print file. Keep an editable copy of your original artwork.</p></article>
      <article class="info-card">{icon("expand")}<h3>Respect the safe area</h3><p>Keep key messages, logos and contact details inside the approved safe area. Extend backgrounds into the specified bleed.</p></article>
      <article class="info-card">{icon("check-circle")}<h3>Send an approval preview</h3><p>Include a JPG preview with the final PDF so the layout can be checked before production.</p></article>
    </div>
    <div class="info-card prose">
      <h2>Layout references</h2>
      <p>The supplied design guide shows the layouts below. These are design references; confirm the available unit and request its final template before printing.</p>
      <figure class="artwork-reference">
        <img src="assets/artwork-reference.svg" width="600" height="860" loading="lazy" decoding="async" alt="Two proportional inflatable billboard layout references: 40 by 22 feet and 20 by 20 feet, with cyan dashed safe-area outlines. Exact safe-area dimensions are listed in the table below.">
        <figcaption>Layout references only. Request the final production template before printing.</figcaption>
      </figure>
      <table class="spec-table">
        <caption>Billboard and safe-area references</caption>
        <thead><tr><th scope="col">Billboard reference</th><th scope="col">Safe-area reference</th></tr></thead>
        <tbody>
          <tr><th scope="row">40 ft × 22 ft</th><td>35.43 ft W × 15.74 ft H</td></tr>
          <tr><th scope="row">20 ft × 20 ft</th><td>17.72 ft W × 14.31 ft H</td></tr>
        </tbody>
      </table>
      <p>Keep file names clear and include your company, campaign name and version. Contact us for the best way to transfer larger production files.</p>
      <a class="button" href="mailto:info@impactair.ca?subject=IMPACTAIR%20artwork%20template%20request">Request an Artwork Template</a>
      <a class="button button-outline" href="mailto:info@impactair.ca?subject=IMPACTAIR%20artwork%20submission">Submit Artwork</a>
    </div>
  </div>
</section>''',
    },
}
