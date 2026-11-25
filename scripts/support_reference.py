"""Live, responsive implementations of the supplied supporting-page designs.

Photographic scenery is selected from the unchanged user-supplied artwork.
Every heading, policy paragraph, form control and dimension remains native text
or SVG. Contact links use the address already established in the repository.
"""
from html import escape


_PATHS = {
    'mail': '<rect x="2" y="4" width="20" height="16" rx="1.5"/><path d="m3 6 9 7 9-7"/>',
    'calendar': '<rect x="3" y="5" width="18" height="16" rx="1.5"/><path d="M7 2v6m10-6v6M3 10h18m-14 4h1m3 0h1m3 0h1m-9 3h1m3 0h1m3 0h1"/>',
    'users': '<circle cx="12" cy="7" r="3.5"/><path d="M5.5 21v-2a6.5 6.5 0 0 1 13 0v2ZM4 5a3 3 0 0 0 0 6m16-6a3 3 0 0 1 0 6M2 20v-3a4 4 0 0 1 3-4m17 7v-3a4 4 0 0 0-3-4"/>',
    'pin': '<path d="M20 9c0 5.3-8 13-8 13S4 14.3 4 9a8 8 0 0 1 16 0Z"/><circle cx="12" cy="9" r="2.7"/>',
    'billboard': '<rect x="2" y="5" width="20" height="13" rx="1"/><path d="M6 2v3m6-3v3m6-3v3M7 18v4m10-4v4"/>',
    'target': '<path d="M21 10a9 9 0 1 1-7-7M17 11a5 5 0 1 1-4-4m-1 5 9-9m-1-2v4h4"/>',
    'handshake': '<path d="m2 10 5-7 5 2 5-2 5 7-4 3-5-5-4 3-2-2 5-5M3 12l7 8 2-1 2 1 2-2 2-2-1-2m-9 1 3-3m0 6 3-3m0 4 2-2"/>',
    'growth': '<path d="M3 21v-7h4v7m3 0V9h4v12m3 0V4h4v17M2 10l7-3 4-4h7m-4-3 4 3-1 4"/>',
    'bulb': '<path d="M8 18c0-4-3-4-3-9a7 7 0 0 1 14 0c0 5-3 5-3 9Zm0 3h8m-6 3h4M12 0v-3M1 3l-2-2m24 2 2-2M0 11h-3m27 0h3M9 9l3 4 3-4m-3 4v5"/>',
    'megaphone': '<path d="M3 9v7h5l13 5V3L8 9H3Zm5 7 2 7h4l-2-6M4 9l-2 1v5l2 1m20-9 3-2m-3 7h4m-4 5 3 2"/>',
    'laptop': '<rect x="4" y="3" width="16" height="14" rx="1"/><path d="M2 18h20l-2 4H4l-2-4Zm7 0h6"/>',
    'shield': '<path d="m12 2 9 4v6c0 5-5 8-9 11-4-3-9-6-9-11V6l9-4Z"/><rect x="9" y="11" width="6" height="6" rx=".6"/><path d="M10 11V9a2 2 0 0 1 4 0v2m-2 3v1"/>',
    'share': '<circle cx="5" cy="12" r="3"/><circle cx="19" cy="4" r="3"/><circle cx="19" cy="20" r="3"/><path d="m8 10 8-4M8 14l8 4"/>',
    'cookie': '<path d="M21 10c-3 1-5-1-5-4-3 0-5-1-5-4A10 10 0 1 0 22 13c-1 0-1-1-1-3Z"/><circle cx="7" cy="10" r="1"/><circle cx="11" cy="17" r="1"/><circle cx="16" cy="13" r="1"/>',
    'document': '<path d="M4 2h11l5 5v6M4 2v20h8M15 2v6h5M7 7h4m-4 5h9m-9 4h4"/><circle cx="18" cy="18" r="5"/><path d="m15.5 18 1.7 1.7 3.4-3.4"/>',
    'refresh': '<path d="M3 9a9 9 0 0 1 16-5l2 3m0-5v5h-5M21 15a9 9 0 0 1-16 5l-2-3m0 5v-5h5"/>',
    'copyright': '<circle cx="12" cy="12" r="10"/><path d="M16 8a5 5 0 1 0 0 8"/>',
    'link': '<path d="m9 8 5-5a5 5 0 0 1 7 7l-5 5M8 9l-5 5a5 5 0 0 0 7 7l5-5M8 16l8-8"/>',
    'check-shield': '<path d="m12 2 9 4v6c0 5-5 8-9 11-4-3-9-6-9-11V6l9-4Z"/><path d="m7 12 4 4 7-8"/>',
    'trim': '<path d="M5 1v19h19M1 5h19v19M1 1v6m0-6h6m16 0v6m0-6h-6M1 23v-6m0 6h6m16 0v-6m0 6h-6"/>',
    'safe': '<rect x="3" y="3" width="18" height="18" rx="1" stroke-dasharray="2.2 2.1"/>',
    'pdf': '<path d="M5 2h10l5 5v15H5ZM15 2v6h5"/><text x="12" y="16" text-anchor="middle" font-family="Arial,sans-serif" font-size="6" font-weight="800" stroke="none" fill="currentColor">PDF</text>',
    'pen': '<path d="M2 3h20m-10 0L5 15l7 8 7-8-7-12Zm0 5v7m-5 4h10"/><circle cx="12" cy="3" r="2"/><circle cx="2" cy="3" r="1"/><circle cx="22" cy="3" r="1"/>',
    'image': '<rect x="2" y="3" width="20" height="18" rx="2"/><path d="m3 18 6-6 4 4 4-6 5 5"/><circle cx="8" cy="8" r="1.3"/>',
    'jpg': '<rect x="2" y="6" width="20" height="13" rx="2"/><path d="M5 6V2h14v4M5 19v4h14v-4"/><text x="12" y="15" text-anchor="middle" font-family="Arial,sans-serif" font-size="7" font-weight="800" stroke="none" fill="currentColor">JPG</text>',
    'warning': '<path d="M11 3a1.3 1.3 0 0 1 2 0l9 17a1.4 1.4 0 0 1-1 2H3a1.4 1.4 0 0 1-1-2Z" fill="currentColor"/><path d="M12 8v6m0 4h.01" stroke="#fff" stroke-width="2.4"/>',
    'send': '<path d="m2 11 20-9-7 20-4-8-9-3Zm9 3L22 2"/>',
    'arrow': '<path d="M2 12h19m-7-7 7 7-7 7"/>',
}


def _icon(name):
    return (f'<svg class="support-icon" aria-hidden="true" viewBox="0 0 24 24" width="64" height="64">'
            f'<g fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{_PATHS[name]}</g></svg>')


def _button(label, href, cls=''):
    return f'<a class="ref-button support-button {cls}" href="{escape(href, quote=True)}">{label}{_icon("arrow")}</a>'


def _waves():
    return '''<svg class="support-waves" viewBox="0 0 1024 100" preserveAspectRatio="none" aria-hidden="true"><path d="M0 83C330 120 812 94 1024 14V68C740 120 300 115 0 89Z" fill="#ff8000"/><path d="M0 76C378 124 815 66 1024 0V24C787 101 299 117 0 84Z" fill="#00bde8"/></svg>'''


def _photo_hero(sheet, heading, intro, height, cls=''):
    # Native 1024×1536 source sheets: show only the original hero photograph.
    position = 54 / (1536 - height) * 100
    return f'''<section class="support-photo-hero {cls}" style="--support-hero-ratio:{height / 1024};--support-sheet:url('references/{sheet}.png');--support-sheet-y:{position:.8f}%;--support-sheet-size:{1536 / height * 100:.8f}%">
      <div class="support-photo-hero-art" aria-hidden="true"></div>
      <div class="support-wrap support-photo-hero-copy"><h1 class="support-slash">{heading}</h1><p>{intro}</p><span class="support-brush" aria-hidden="true"></span></div>
    </section>'''


def _plain_banner(heading, intro, cls=''):
    return f'''<section class="support-plain-banner {cls}"><div class="support-wrap"><h1 class="support-slash">{heading}</h1><p>{intro}</p></div>{_waves()}</section>'''


def _feature_strip(items, cls=''):
    return f'''<section class="support-feature-strip {cls}"><div class="support-wrap">{''.join(f'<div class="support-strip-item">{_icon(name)}<span>{label}</span></div>' for name, label in items)}</div>{_waves()}</section>'''


def _legal_footer(topic):
    return f'''<section class="support-legal-footer"><div class="support-wrap"><h2 class="support-slash">Questions About<br>Our <em>{topic}?</em></h2><div class="support-legal-contact">{_icon('mail')}<p>Contact us at<br><a href="mailto:info@impactair.ca">info@impactair.ca</a><br>for more information.</p></div></div>{_waves()}</section>'''


def _legal_rows(rows):
    return '<div class="support-legal-rows">' + ''.join(
        f'<section class="support-legal-row">{_icon(name)}<div><h2>{title}</h2><p>{copy}</p></div></section>'
        for name, title, copy in rows
    ) + '</div>'


PRIVACY_ROWS = [
    ('users', 'Information We Collect', 'We may collect personal information such as your name, company, email address, phone number and any other details you provide through our website, forms or communications.'),
    ('laptop', 'How We Use Your Information', 'We use your information to respond to inquiries, provide quotes, deliver our services, share relevant updates and improve your website experience.'),
    ('shield', 'How We Protect Your Information', 'We use appropriate security measures to protect your personal information from unauthorized access, disclosure or misuse.'),
    ('share', 'Sharing Your Information', 'We do not sell or rent your personal information. We may only share it with trusted service providers who help us operate our business (such as website hosting, email communications or analytics), and only for those specific purposes.'),
    ('cookie', 'Cookies and Tracking', 'Our website may use cookies and similar technologies to enhance your experience, understand website usage and improve our services. You can adjust your browser settings to manage cookies.'),
    ('document', 'Your Choices', 'You can contact us at any time to update, correct or request the removal of your personal information from our records, subject to legal or business requirements.'),
    ('refresh', 'Changes to This Policy', 'We may update this Privacy Policy from time to time. Any changes will be posted on this page with a new “Last Updated” date.'),
]

TERMS_ROWS = [
    ('handshake', '1. Acceptance of Terms', 'By using this website, you agree to these Terms of Use and our <a href="privacy-policy.html">Privacy Policy</a>, which together govern your use of the site and our services.'),
    ('laptop', '2. Use of Our Website', 'You agree to use this website for lawful purposes only and in a way that does not interfere with the site’s operation, security or the experience of others.'),
    ('copyright', '3. Intellectual Property', 'All content on this website, including text, graphics, logos, images, videos and design, is the property of ImpactAir or its licensors and is protected by applicable copyright, trademark and other laws. You may not copy, reproduce or use this content without our prior written permission.'),
    ('document', '4. Services and Information', 'The information on this website is for general informational purposes about our outdoor advertising and event marketing services. We make reasonable efforts to keep it accurate and up to date, but we do not guarantee that it is complete, current or error-free.'),
    ('link', '5. Third-Party Links', 'Our website may contain links to third-party websites. We are not responsible for the content, policies or practices of those websites.'),
    ('check-shield', '6. Limitation of Liability', 'ImpactAir is not liable for any direct, indirect, incidental or consequential damages arising from your use of this website or reliance on its content, to the fullest extent permitted by law.'),
    ('refresh', '7. Changes to These Terms', 'We may update these Terms of Use from time to time. Any changes will be posted on this page with a new “Last Updated” date. Your continued use of the website after changes are posted means you accept the revised terms.'),
    ('mail', '8. Contact Us', 'If you have any questions about these Terms of Use, please contact us at <a href="mailto:info@impactair.ca"><strong>info@impactair.ca.</strong></a>'),
]


def _page(title, description, body, cls):
    return {'title': title, 'description': description, 'custom_layout': True,
            'extra_css': 'assets/support-reference.css',
            'body': f'<div class="reference-page support-reference {cls}">{body}</div>'}


CONTACT_FORM = f'''<form class="quote-form support-quote" id="quote" action="mailto:info@impactair.ca" method="post" enctype="text/plain" data-email="info@impactair.ca">
  <h2 class="support-slash">Send Us a Message</h2><p class="support-form-intro">Tell us about your advertising goals and we’ll get back to you soon.</p>
  <div class="support-form-fields">
    <label class="support-field-wide"><span class="sr-only">Your name (required)</span><input name="name" autocomplete="name" maxlength="120" placeholder="Your Name *" required></label>
    <label class="support-field-wide"><span class="sr-only">Company or organization (required)</span><input name="company" autocomplete="organization" maxlength="160" placeholder="Company / Organization *" required></label>
    <label><span class="sr-only">Email (required)</span><input name="email" type="email" autocomplete="email" maxlength="254" placeholder="Email *" required></label>
    <label><span class="sr-only">Phone</span><input name="phone" type="tel" autocomplete="tel" maxlength="40" placeholder="Phone"></label>
    <label class="support-field-wide support-select"><span class="sr-only">I’m interested in (required)</span><select name="interest" required><option value="">I’m Interested In *</option><option value="festival-advertising">Festival Advertising</option><option value="billboards">Inflatable Billboards</option><option value="event-branding">Event Branding</option><option value="multi-event">Multi-Event Campaigns</option><option value="music">Music &amp; Entertainment</option><option value="food">Food &amp; Culinary</option><option value="culture">Caribbean &amp; Multicultural</option><option value="community">Community Festivals</option><option value="media-proposal">2027 Media Proposal</option><option value="festival-list">Full Festival List</option><option value="festival-partnership">Festival Partnership</option><option value="other">Other Enquiry</option></select></label>
    <label class="support-field-wide"><span class="sr-only">Event date or campaign period (optional)</span><input name="event-date" maxlength="160" placeholder="Event Date / Campaign Period (Optional)"></label>
    <label class="support-field-wide"><span class="sr-only">Your message (required)</span><textarea name="message" rows="4" maxlength="4000" placeholder="Your Message *" required></textarea></label>
  </div>
  <button class="ref-button support-button support-send" type="submit">{_icon('send')}Send Message</button>
  <p class="support-form-note">Opens a draft in your email app for you to review and send. <a href="privacy-policy.html">Privacy Policy</a></p>
  <p class="form-status" id="quote-status" role="status" aria-live="polite"></p>
  <noscript><p class="support-form-note">Send the form with your email app, or email <a href="mailto:info@impactair.ca">info@impactair.ca</a>.</p></noscript>
</form>'''


CONTACT_BODY = (
    _photo_hero('contact', 'CONTACT <em>US</em>', 'Let’s bring your brand to<br>Ontario’s biggest festivals<br>and events.', 334, 'support-contact-hero')
    + _feature_strip([('calendar','Festival<br>Advertising'), ('billboard','Inflatable<br>Billboards'), ('pin','Event<br>Branding'), ('users','Multi-Event<br>Campaigns')], 'support-contact-strip')
    + f'''<section class="support-contact-main"><div class="support-contact-grid">{CONTACT_FORM}
      <aside class="support-get-in-touch"><h2 class="support-slash">Get in Touch</h2>
        <div class="support-contact-method">{_icon('mail')}<div><h3>Email Us</h3><a href="mailto:info@impactair.ca">info@impactair.ca</a></div></div>
        <div class="support-contact-method">{_icon('pin')}<div><h3>Service Area</h3><p>Toronto (GTA) and<br>across Ontario</p></div></div>
        <div class="support-contact-method">{_icon('calendar')}<div><h3>Festival Season</h3><p>June – September<br>2027</p></div></div>
        <div class="support-contact-resources"><h2 class="support-slash">Plan Your Campaign</h2><a href="2027-festival-opportunities.html">2027 Festival Opportunities {_icon('arrow')}</a><a href="artwork-specifications.html">Artwork Specifications {_icon('arrow')}</a></div>
      </aside></div>{_waves()}</section>
      <section class="support-contact-why"><div class="support-wrap"><h2 class="support-slash">Why Contact <em>IMPACTAIR?</em></h2><div class="support-contact-reasons">
        <article>{_icon('handshake')}<div><h3>Get Expert Guidance</h3><p>on your festival advertising options.</p></div></article>
        <article>{_icon('calendar')}<div><h3>Find the Right Events</h3><p>for your brand and audience.</p></div></article>
        <article>{_icon('target')}<div><h3>Customized Campaigns</h3><p>to meet your marketing goals.</p></div></article>
      </div></div></section>
      <section class="support-contact-cta"><div class="support-contact-cta-art" aria-hidden="true"></div><div class="support-wrap"><div><h2>Ready to Be Seen<br>at <strong>Ontario’s Top Festivals?</strong></h2>{_button('Request a 2027 Media Proposal', 'contact.html?interest=media-proposal#quote')}</div></div></section>'''
)


CAREER_ROLES = [
    ('growth', 'Sales<br>Executives', 'Build client relationships and drive new business and partnerships.', 'cyan'),
    ('bulb', 'Creative<br>Talent', 'Bring fresh ideas to brand activations and event experiences.', 'violet'),
    ('users', 'Event<br>Professionals', 'Support on-site activations and festival operations.', 'cyan'),
    ('megaphone', 'Marketing &amp;<br>Promotions', 'Help grow our brand, create awareness and engage audiences.', 'orange'),
]

CAREERS_BODY = (
    _photo_hero('careers', 'CAREERS<br><span>AT <em>IMPACTAIR</em></span>', 'Have Talent? Drive Sales?<br><strong>We Want You!</strong>', 392, 'support-careers-hero')
    + '''<section class="support-careers-intro"><div class="support-wrap"><h2 class="support-slash">Bring Your <em>Talent</em> to Our Team</h2><p>ImpactAir is always looking for motivated, creative and results-driven people<br>to help us grow across Ontario’s biggest festivals and events.</p></div></section>'''
    + _feature_strip([('calendar','Major<br>Festivals'), ('users','High-Visibility<br>Campaigns'), ('growth','Growth<br>Opportunities'), ('handshake','Work With<br>Leading Brands')], 'support-careers-strip')
    + f'''<section class="support-careers-roles"><div class="support-careers-heading support-wrap"><h2 class="support-slash">We’re Looking for<br>People Like <strong>You!</strong></h2><p>If you have the skills, experience or passion for sales, marketing, event activation or creative execution, we’d love to hear from you.</p></div><div class="support-role-grid">{''.join(f'<article class="support-role-card support-role-{color}">{_icon(name)}<h3>{title}</h3><span class="support-role-rule" aria-hidden="true"></span><p>{copy}</p></article>' for name,title,copy,color in CAREER_ROLES)}</div></section>
    <section class="support-careers-apply"><div class="support-wrap"><div class="support-apply-heading"><h2 class="support-slash">Tell Us About<br>Your <em>Talent</em></h2><p>Ready to make an impact at<br>Ontario’s top festivals and events?<br>Send us your résumé and let’s talk.</p></div>{_button('Apply Now', 'mailto:info@impactair.ca?subject=IMPACTAIR%20careers%20enquiry')}</div>{_waves()}</section>'''
)


ARTWORK_REQUIREMENTS = [
    ('trim', 'Trim Area', '<strong>40′ W × 22′ H<br>or<br>20′ W × 20′ H</strong>'),
    ('safe', 'Safe Area', '<strong>35.43′ W × 15.74′ H</strong><br>(40′ × 22′)<hr><strong>17.72′ W × 14.31′ H</strong><br>(20′ × 20′)'),
    ('pdf', 'Artwork<br>Format', 'All artwork must be supplied as a high-resolution, print-ready PDF.'),
    ('pen', 'Text', 'All text must be converted to outlined vectors, ready to scale for large-format printing.'),
    ('image', 'Images', '<strong>CMYK</strong><br>300 DPI minimum at 1:20 scale.'),
    ('jpg', 'Preview', 'Please provide a low-resolution JPG of your final creative for reference and approval.'),
]

ARTWORK_BODY = (
    _plain_banner('ARTWORK<br><em>SPECIFICATIONS</em>', 'Design Guidelines for Inflatable Billboards', 'support-artwork-banner')
    + f'''<section class="support-artwork-diagrams"><figure class="support-diagram-wide"><h2>40′ × 22′ Inflatable Billboard</h2><svg role="img" aria-labelledby="wide-artwork-title" viewBox="0 0 600 450"><title id="wide-artwork-title">40 foot wide by 22 foot high inflatable billboard. Safe area 35.43 feet wide by 15.74 feet high.</title><use href="assets/artwork-diagrams.svg#wide"></use></svg></figure><figure class="support-diagram-square"><h2>20′ × 20′ Inflatable Billboard</h2><svg role="img" aria-labelledby="square-artwork-title" viewBox="0 0 400 450"><title id="square-artwork-title">20 foot wide by 20 foot high inflatable billboard. Safe area 17.72 feet wide by 14.31 feet high.</title><use href="assets/artwork-diagrams.svg#square"></use></svg></figure></section>
    <section class="support-artwork-requirements"><h2 class="support-slash">Artwork <em>Submission Requirements</em></h2><div class="support-requirements-grid">{''.join(f'<article>{_icon(name)}<h3>{title}</h3><p>{copy}</p></article>' for name,title,copy in ARTWORK_REQUIREMENTS)}</div></section>
    <aside class="support-artwork-important">{_icon('warning')}<p><strong>IMPORTANT:</strong> Keep all logos, text and essential design elements within the designated safe area. Extend background artwork to the full trim area.</p></aside>
    <section class="support-artwork-submit">{_button('Submit Artwork', 'mailto:info@impactair.ca?subject=IMPACTAIR%20artwork%20submission')}{_waves()}</section>'''
)


SUPPORT_REFERENCE = {
    'contact.html': _page('Contact Us & Request a Quote', 'Bring your brand to Ontario’s biggest festivals and events. Contact IMPACTAIR for inflatable billboards, festival advertising and 2027 media proposals.', CONTACT_BODY, 'support-contact'),
    'careers.html': _page('Careers at IMPACTAIR', 'Bring your talent to the IMPACTAIR team. Introduce your skills in sales, creative work, event operations, marketing and promotions.', CAREERS_BODY, 'support-careers'),
    'privacy-policy.html': _page('Privacy Policy', 'How ImpactAir collects, uses and protects your information.',
        _plain_banner('Privacy <em>Policy</em>', 'How we collect, use and protect your information.')
        + '<article class="support-legal-content support-wrap"><div class="support-legal-intro"><p><strong>Last Updated: November 22, 2026</strong></p><p>At ImpactAir, we are committed to protecting your privacy. This Privacy Policy explains how we collect, use, store and safeguard your personal information when you visit our website, contact us or use our services.</p></div>'
        + _legal_rows(PRIVACY_ROWS) + '</article>' + _legal_footer('Privacy Policy'), 'support-legal support-privacy'),
    'terms-of-use.html': _page('Terms of Use', 'The rules for using the ImpactAir website and services.',
        _plain_banner('Terms of <em>Use</em>', 'The rules for using the ImpactAir website and services.')
        + '<article class="support-legal-content support-wrap"><div class="support-legal-intro"><p><strong>Last Updated: November 22, 2026</strong></p><p>Welcome to the ImpactAir website. By accessing or using this website, you agree to the following Terms of Use. If you do not agree, please do not use our website.</p></div>'
        + _legal_rows(TERMS_ROWS) + '</article>' + _legal_footer('Terms of Use'), 'support-legal support-terms'),
    'artwork-specifications.html': _page('Artwork Specifications', 'Design guidelines for IMPACTAIR inflatable billboards: trim dimensions, safe areas, print-ready PDF files, outlined text, CMYK images and preview requirements.', ARTWORK_BODY, 'support-artwork'),
}
