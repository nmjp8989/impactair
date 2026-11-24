"""Content for the six primary pages in the supplied ImpactAir design."""


def icon(name):
    return f'<svg class="icon" aria-hidden="true" width="24" height="24"><use href="assets/icons.svg#{name}"></use></svg>'


def image(name, alt, extra=''):
    names = {'hero-festival.png':'hero-festival.webp', 'design-music.webp':'festival-music.webp',
             'design-food.webp':'festival-food.webp', 'design-culture.webp':'festival-culture.webp',
             'design-community.webp':'festival-community.webp'}
    name = names.get(name, name)
    w, h = (1672, 941) if name == 'hero-festival.webp' else (1536, 1024)
    stem = name.removesuffix('.webp')
    sources = f'assets/{stem}-768.webp 768w, assets/{stem}-1280.webp 1280w, assets/{name} {w}w'
    # The sizing hint accounts for cover-cropping, so retina displays get enough pixels.
    return f'<img src="assets/{name}" srcset="{sources}" sizes="800px" width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async" {extra}>'


def planning_strip():
    return f'''<section class="planning-strip" aria-label="Campaign planning">
      <div class="wrap planning-grid">
        <div>{icon('calendar')}<p><strong>2027</strong><span>Festival opportunities</span></p></div>
        <div>{icon('users')}<p><strong>Ontario</strong><span>Big events. Engaged audiences.</span></p></div>
        <div>{icon('pin')}<p><strong>June–Sept</strong><span>Plan your summer campaign</span></p></div>
      </div>
    </section>'''


CATEGORIES = [
    ('music', 'Music &amp;<br>Entertainment', 'Concerts, live performances and the energy of summer.', 'design-music.webp', 'Purple stage lights above an outdoor concert audience', 'music'),
    ('food', 'Food &amp;<br>Culinary', 'Food festivals, local flavours and shared experiences.', 'design-food.webp', 'Food stalls and festival visitors beneath warm string lights', 'food'),
    ('culture', 'Caribbean &amp;<br>Multicultural', 'Heritage, culture and celebrations that bring people together.', 'design-culture.webp', 'Carnival performers wearing colourful feathered costumes', 'culture'),
    ('community', 'Community<br>Festivals', 'Local events and meaningful connections across Ontario.', 'design-community.webp', 'Visitors and tents at a sunny community festival', 'community'),
]


def category_grid(full=False):
    cards = []
    for key, title, copy, asset, alt, color in CATEGORIES:
        link = f'contact.html?interest={key}#quote' if full else f'festival-categories.html#{key}'
        cards.append(f'''<article class="category-card category-{color}" id="{key}">
          {image(asset, alt)}
          <div class="category-copy"><h3>{title}</h3><p>{copy}</p>
            <a href="{link}">{'Discuss This Category' if full else 'Explore Category'}<span class="sr-only">: {title.replace('<br>', ' ')}</span></a>
          </div>
        </article>''')
    return '<div class="category-grid' + (' category-grid-detailed' if full else '') + '">' + ''.join(cards) + '</div>'


def cta(title='Be part of Ontario’s<br><em>biggest events.</em>', text='Give your brand a bigger presence. Let’s plan your next campaign.', button='Request a Quote', href='contact.html#quote'):
    return f'''<section class="section cta-section"><div class="wrap campaign-cta">
      <div class="cta-image">{image('design-music.webp', '')}</div>
      <div class="cta-copy"><h2>{title}</h2><p>{text}</p><a class="button" href="{href}">{button}</a></div>
    </div></section>'''


MAIN_PAGES = {
    'index.html': {
        'title': 'Inflatable Billboard Advertising in Ontario',
        'description': 'Bigger brands. Bolder events. Higher impact. Explore IMPACTAIR inflatable billboard advertising for Ontario festivals and 2027 campaigns.',
        'heading': 'Bigger brands.<br>Bolder events.<br><em>Higher impact.</em>',
        'kicker': 'Inflatable billboard advertising',
        'intro': 'Put your brand at the heart of Ontario’s biggest festivals and events.',
        'hero': 'home',
        'actions': [('Request a Quote', 'contact.html#quote', ''), ('Explore 2027 Opportunities', '2027-festival-opportunities.html', 'button-outline')],
        'body': planning_strip() + f'''
<section class="section why-section"><div class="wrap">
  <div class="section-heading"><p class="eyebrow">Make your presence felt</p><h2>Why choose <em>ImpactAir?</em></h2><p>Stand out in the crowd. Be part of the experience.</p></div>
  <div class="benefit-grid">
    <article class="benefit-card">{icon('eye')}<div><h3>Maximum visibility</h3><p>Big, bold branding that rises above the crowd and gets your message seen.</p></div></article>
    <article class="benefit-card">{icon('calendar')}<div><h3>Event flexibility</h3><p>From concerts to cultural celebrations, build a campaign around your audience.</p></div></article>
    <article class="benefit-card">{icon('target')}<div><h3>Meaningful connections</h3><p>Bring your brand into the moments people come together to enjoy.</p></div></article>
  </div>
  <a class="text-link" href="benefits.html">Discover the Benefits</a>
</div></section>
<section class="section section-tint"><div class="wrap">
  <div class="section-heading heading-row"><div><p class="eyebrow">Find your audience</p><h2>Big events.<br><em>Even bigger possibilities.</em></h2></div><a class="button button-dark" href="festival-categories.html">Explore Festival Categories</a></div>
  {category_grid()}
</div></section>''' + cta(),
    },
    'about.html': {
        'title': 'About Us',
        'description': 'IMPACTAIR helps brands get noticed with inflatable billboard advertising at festivals, events and high-traffic locations across Ontario.',
        'heading': 'About <em>Us.</em>',
        'kicker': 'About us',
        'intro': 'Inflatable billboard advertising built for Ontario’s festivals and events.',
        'hero': 'compact',
        'body': f'''<section class="section"><div class="wrap split-section">
  <div class="section-copy"><p class="eyebrow">Who we are</p><h2>We help brands<br><em>stand out.</em></h2><p>IMPACTAIR specializes in high-impact inflatable billboard rentals for festivals, events and high-traffic locations across Ontario.</p><p>We combine bold creative with a visible event presence, helping your message become part of the experience. From your first idea to the details of your installation, we’ll help you plan a campaign that fits.</p><a class="button" href="contact.html#quote">Let’s Talk About Your Brand</a></div>
  <figure class="feature-photo">{image('hero-festival.png', 'An IMPACTAIR inflatable billboard in a Toronto festival setting')}<figcaption>Big branding. Memorable festival moments.</figcaption></figure>
</div></section>
<section class="section section-tint"><div class="wrap"><div class="benefit-grid">
  <article class="benefit-card">{icon('target')}<div><h3>Our mission</h3><p>Create bold, memorable brand experiences.</p></div></article>
  <article class="benefit-card">{icon('eye')}<div><h3>Our vision</h3><p>Build Ontario’s leading inflatable advertising network.</p></div></article>
  <article class="benefit-card">{icon('handshake')}<div><h3>Our commitment</h3><p>Bring quality, care and reliability to every installation.</p></div></article>
</div></div></section>''' + cta('Your brand.<br><em>Our next big idea.</em>', 'Tell us what you have in mind. We’ll help you explore the possibilities.'),
    },
    'benefits.html': {
        'title': 'The Benefits of IMPACTAIR Advertising',
        'description': 'Discover how inflatable billboard advertising brings visibility, flexibility and a distinctive brand presence to Ontario events.',
        'heading': 'The benefits of<br><em>ImpactAir.</em>',
        'kicker': 'The benefits of ImpactAir',
        'intro': 'Get noticed. Start conversations. Give your audience something to remember.',
        'hero': 'compact',
        'body': '''<section class="section"><div class="wrap benefits-layout"><div class="section-heading"><p class="eyebrow">Built to be seen</p><h2>More than a billboard.<br><em>A brand experience.</em></h2><p>Connect your message with the energy of a live event.</p></div><div class="feature-list">''' + ''.join(
            f'<article class="benefit-card">{icon(i)}<div><h3>{h}</h3><p>{p}</p></div></article>' for i,h,p in [
                ('users', 'Audience reach', 'Bring your brand to lively festival environments and the communities that matter to your campaign.'),
                ('eye', 'High-visibility impact', 'Large-format inflatable billboards give your message a distinctive presence above the crowd.'),
                ('pin', 'Event locations', 'Explore event settings across Ontario and agree the right placement for your campaign.'),
                ('calendar', 'Flexible campaigns', 'Plan a single event or a series of activations around your audience, timing and goals.'),
                ('target', 'Clear campaign goals', 'Discuss what success looks like, from brand awareness to conversations, enquiries and on-site engagement.'),
            ]) + '''</div></div></section>''' + cta('Put your brand<br><em>in the spotlight.</em>', 'Let’s find the right event, audience and format for your next campaign.', 'View Festival Opportunities', '2027-festival-opportunities.html'),
    },
    'festivals.html': {
        'title': 'Festivals & Events',
        'description': 'Explore inflatable billboard advertising for music, food, cultural and community festivals across Ontario.',
        'heading': 'Festivals<br><em>&amp; events.</em>',
        'kicker': 'Festivals & events',
        'intro': 'Connect your brand with the audiences, experiences and communities that make Ontario’s events unforgettable.',
        'hero': 'compact',
        'actions': [('Explore 2027 Opportunities', '2027-festival-opportunities.html', '')],
        'body': planning_strip() + f'''<section class="section"><div class="wrap"><div class="section-heading"><p class="eyebrow">Where your brand belongs</p><h2>A festival for<br><em>every audience.</em></h2><p>Choose the settings that fit your brand and build a campaign around them.</p></div>{category_grid()}</div></section>
<section class="section section-tint"><div class="wrap split-section"><div class="section-copy"><p class="eyebrow">Across Ontario</p><h2>Local connections.<br><em>Wider reach.</em></h2><p>From Toronto and the GTA to Hamilton, Oakville, Burlington, Kitchener and surrounding communities, start a conversation about where your brand wants to be seen.</p><p>Our team can discuss event participation, placement options and current availability in your proposal.</p></div><div class="location-panel">{icon('pin')}<h3>Your next campaign<br>starts here.</h3><ul class="location-list"><li>Toronto &amp; the GTA</li><li>Hamilton</li><li>Oakville</li><li>Burlington</li><li>Kitchener</li><li>Across Ontario</li></ul></div></div></section>''' + cta('Let’s plan your<br><em>2027 presence.</em>', 'Ask for a proposal with event options, timing and availability for your brand.', 'Request a 2027 Media Proposal', 'contact.html?interest=media-proposal#quote'),
    },
    '2027-festival-opportunities.html': {
        'title': '2027 Festival Opportunities',
        'description': 'Plan your 2027 Ontario festival advertising with IMPACTAIR. Explore music, food, cultural and community campaign opportunities.',
        'heading': 'Festival<br><em>opportunities.</em>',
        'kicker': '2027',
        'intro': 'Make next summer your brand’s big moment. Explore inflatable billboard advertising across Ontario.',
        'hero': 'opportunities',
        'actions': [('Request a Media Proposal', 'contact.html?interest=media-proposal#quote', ''), ('Explore Festival Categories', '#opportunities', 'button-outline')],
        'body': planning_strip() + f'''<section class="section" id="opportunities"><div class="wrap"><div class="section-heading"><p class="eyebrow">Plan your campaign</p><h2>Find your moment.<br><em>Make it count.</em></h2><p>Explore the festival categories below, then tell us about your audience and goals.</p></div>{category_grid()}<p class="availability-note">2027 event participation, dates, audience estimates and placements are confirmed in your media proposal. Contact us for current availability.</p></div></section>
<section class="section section-tint"><div class="wrap"><div class="section-heading"><h2>A clear path to<br><em>your next campaign.</em></h2></div><div class="card-grid three-columns"><article class="info-card">{icon('messages')}<h3>Share your goals</h3><p>Tell us about your brand, target audience, campaign timing and preferred locations.</p></article><article class="info-card">{icon('calendar')}<h3>Explore your options</h3><p>Discuss suitable festivals, placements and available billboard formats.</p></article><article class="info-card">{icon('image')}<h3>Bring it to life</h3><p>Confirm your plan, prepare your artwork and coordinate the event details.</p></article></div></div></section>''' + cta('Become a<br><em>festival partner.</em>', 'Organizing an event? Let’s talk about creating a bigger brand presence together.', 'Partner With Us', 'contact.html?interest=festival-partnership#quote'),
    },
    'festival-categories.html': {
        'title': 'Festival Categories',
        'description': 'Explore music, food, Caribbean, multicultural and community festival advertising opportunities with IMPACTAIR.',
        'heading': 'Festival<br><em>categories.</em>',
        'kicker': 'Festival categories',
        'intro': 'A diverse mix of experiences that connect your brand with audiences across Ontario.',
        'hero': 'compact',
        'body': f'''<section class="section"><div class="wrap"><div class="section-heading"><p class="eyebrow">Explore the possibilities</p><h2>Find the right<br><em>audience for your brand.</em></h2></div>{category_grid(True)}</div></section>
<section class="section section-tint"><div class="wrap"><div class="section-heading"><h2>And there’s <em>more.</em></h2><p>Have a different event in mind? Let’s explore what’s possible.</p></div><div class="other-categories"><span>{icon('image')}Arts &amp; Culture</span><span>{icon('target')}Sports &amp; Active Living</span><span>{icon('users')}Health &amp; Wellness</span></div></div></section>''' + cta('One brand.<br><em>Multiple festivals.</em>', 'Build a campaign that carries your message across more than one experience.', 'Request a Media Proposal', 'contact.html?interest=media-proposal#quote'),
    },
}
