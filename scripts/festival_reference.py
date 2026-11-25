"""Festival pages reconstructed from the user's desktop references.

Typography and controls are live HTML. The photographs are native-resolution
regions of the supplied artwork; no screenshot text is used as page content.
"""
from design_common import icon, photo, hero, stats, button, strip


def page(title, description, body):
    return {
        'title': title, 'description': description, 'custom_layout': True,
        'extra_css': 'assets/festival-reference.css',
        'body': body,
    }


def heading(text, cls=''):
    return f'<h2 class="ref-title festival-section-title {cls}">{text}</h2>'


FESTIVAL_ADVANTAGES = [
    ('users', 'Large<br>Audiences'),
    ('target', 'Higher<br>Engagement'),
    ('users', 'Millennial<br>Reach'),
    ('music', 'Music &amp;<br>Food Culture'),
    ('megaphone', 'Big<br>Brand Visibility'),
]


WHY_FESTIVALS = f'''
<div class="reference-page festival-reference">
  {hero('festivals', 'WHY<br><em>FESTIVALS?</em>', 'Massive audiences. High energy.<br>Big opportunities for your brand.', y=54, h=341, cls='festival-hero', kicker='FESTIVALS')}
  <div class="festival-content">
    <section class="festival-proof" aria-label="Why advertise at festivals">
      <div class="ref-wrap"><ul class="festival-proof-list">
        <li>{icon('check')}<span>Growing festivals.</span></li>
        <li>{icon('check')}<span>A younger, hard-to-reach<br class="festival-desktop-break"> millennial audience.</span></li>
        <li>{icon('check')}<span>A powerful way to put<br class="festival-desktop-break"> your brand in front of<br class="festival-desktop-break"> millions.</span></li>
      </ul></div>
      {photo('festivals', 433, 406, 591, 335, 'An illuminated IMPACTAIR Music Festival billboard beside a colourful concert stage and audience.', 'festival-proof-photo')}
    </section>
    <section class="festival-advantage">
      {heading('THE FESTIVAL <em>ADVANTAGE</em>')}
      {strip(FESTIVAL_ADVANTAGES, 'festival-advantage-strip')}
    </section>
    {stats('festival-season-stats')}
  </div>
  <section class="festival-sunset">
    {photo('festivals', 0, 1105, 1024, 290, '', 'festival-sunset-photo')}
    <div class="ref-wrap"><h2>BE PART OF<br>ONTARIO’S BIGGEST<br><span>FESTIVAL SEASON.</span></h2></div>
  </section>
  <section class="festival-bottom-cta">
    <div class="ref-wrap"><h2>THE FESTIVAL AUDIENCE IS READY.<br><em>MAKE SURE YOUR BRAND IS THERE.</em></h2>
      {button('Request a Quote', 'contact.html?interest=festivals#quote')}
    </div>
  </section>
</div>
'''


OPPORTUNITIES = [
    ('Taste of the Danforth', 'TASTE OF<br>THE DANFORTH', 'danforth', 8, 710, 251, 200, 'A busy summer street festival with food tents and crowds.'),
    ('Beaches Jazz Fest', 'BEACHES<br>JAZZ FEST', 'beaches-jazz', 275, 710, 243, 200, 'A lively music stage illuminated with purple concert lights.'),
    ('Toronto Food Festival', 'TORONTO<br>FOOD FESTIVAL', 'toronto-food', 527, 710, 252, 200, 'Festival visitors enjoying food at an outdoor food festival.'),
    ('Caribbean Festivals', 'CARIBBEAN<br>FESTIVALS', 'caribbean', 788, 710, 228, 200, 'A smiling Caribbean carnival performer wearing a bright feathered costume.'),
]


def opportunity_cards():
    return '<div class="opportunity-cards">' + ''.join(
        f'''<a class="opportunity-card" href="contact.html?interest={key}#quote" aria-label="Enquire about {name}">
          {photo('opportunities', x, y, w, h, alt, 'opportunity-card-photo')}
          <div class="opportunity-card-copy"><h3>{title}</h3><span class="opportunity-card-line" aria-hidden="true"></span></div>
        </a>'''
        for name, title, key, x, y, w, h, alt in OPPORTUNITIES
    ) + '</div>'


COVERAGE = ['Toronto<br>(GTA)', 'Hamilton', 'Oakville', 'Burlington', 'Kitchener<br>&amp; More']
INCLUDED = [
    ('billboard', 'Inflatable<br>Billboards'),
    ('lightbulb', 'Illuminated<br>Options'),
    ('pin', 'Prime<br>Event Locations'),
    ('truck', 'Delivery,<br>Setup &amp; Removal'),
    ('users', 'On-Site<br>Support'),
]


OPPORTUNITIES_PAGE = f'''
<div class="reference-page opportunities-reference">
  {hero('opportunities', 'FESTIVAL<br><em>OPPORTUNITIES</em>', 'Put your brand in front of<br>millions at Ontario’s top<br>festivals and events.', y=54, h=411, cls='opportunities-hero', kicker='2027')}
  <div class="festival-content">
    {stats('opportunities-stats')}
    <section class="opportunities-featured" id="featured-festivals">
      {heading('FEATURED FESTIVAL OPPORTUNITIES')}
      {opportunity_cards()}
    </section>
    <section class="opportunities-coverage" aria-label="Event coverage across Ontario">
      <h2>{icon('pin')}<span>EVENT COVERAGE<br>ACROSS ONTARIO</span></h2>
      <ul>{''.join(f'<li>{icon("check-circle")}<span>{place}</span></li>' for place in COVERAGE)}</ul>
    </section>
    <section class="opportunities-included" aria-labelledby="included-heading">
      <h2 class="ref-title" id="included-heading">WHAT’S<br>INCLUDED?</h2>
      {strip(INCLUDED, 'opportunities-included-strip')}
    </section>
  </div>
  <section class="opportunities-final">
    {photo('opportunities', 0, 1275, 1024, 261, '', 'opportunities-final-photo')}
    <div class="ref-wrap">
      <h2>SECURE YOUR<br>SPOT FOR THE<br><em>2027</em> FESTIVAL<br>SEASON.</h2>
      <div class="opportunities-final-actions">
        {button('Request a Quote', 'contact.html?interest=2027#quote')}
        <a class="ref-button ref-button-outline festival-list-link" href="contact.html?interest=festival-list#quote">{icon('calendar')}<span>Request Full Festival List</span></a>
      </div>
    </div>
  </section>
</div>
'''


CATEGORY_FEATURES = [
    ('users', 'Diverse<br>Audiences'),
    ('pin', 'High-Traffic<br>Locations'),
    ('megaphone', 'Premium<br>Brand Exposure'),
    ('trending-up', 'Measurable<br>Impact'),
]

CATEGORIES = [
    ('music', 'Music & Entertainment', 'MUSIC &amp;<br>ENTERTAINMENT', 'Concerts, live performances<br>and major summer events.', 'music', 16, 622, 488, 118, 'A cheering concert crowd beneath purple and blue stage lights.'),
    ('food', 'Food & Culinary', 'FOOD &amp;<br>CULINARY', 'Food festivals, street food<br>events and culinary experiences.', 'food', 521, 622, 488, 118, 'Freshly grilled food topped with herbs at a culinary festival.'),
    ('culture', 'Caribbean & Multicultural', 'CARIBBEAN &amp;<br>MULTICULTURAL', 'Caribbean events, heritage festivals<br>and multicultural celebrations.', 'palm', 16, 874, 488, 128, 'A Caribbean carnival performer in a colourful feathered headdress.'),
    ('community', 'Community Festivals', 'COMMUNITY<br>FESTIVALS', 'Local, cultural and community events<br>that bring people together.', 'users', 521, 874, 488, 128, 'A father carrying his smiling daughter on his shoulders at a community festival.'),
]


def category_cards():
    return '<div class="festival-category-grid">' + ''.join(
        f'''<a class="festival-category-card festival-category-{key}" id="{key}" href="contact.html?interest={key}#quote" aria-label="Discuss {name}">
          {photo('categories', x, y, w, h, alt, 'festival-category-photo')}
          <div class="festival-category-copy"><span class="festival-category-badge">{icon(symbol)}</span><div><h3>{title}</h3><p>{copy}</p></div>{icon('arrow-right')}</div>
        </a>'''
        for key, name, title, copy, symbol, x, y, w, h, alt in CATEGORIES
    ) + '</div>'


OTHER_CATEGORIES = [
    ('theatre', 'Arts &amp;<br>Culture', 'arts-culture'),
    ('activity', 'Sports &amp;<br>Active Living', 'sports'),
    ('leaf', 'Health &amp;<br>Wellness', 'wellness'),
    ('users', 'Family<br>&amp; Lifestyle', 'family'),
]


CATEGORIES_PAGE = f'''
<div class="reference-page categories-reference">
  {hero('categories', 'Festival<br><em>Categories</em>', 'A diverse mix of events that connect<br>your brand with millions across Ontario.', y=55, h=342, cls='categories-hero')}
  <div class="festival-content">
    {strip(CATEGORY_FEATURES, 'festival-categories-features')}
    <section class="festival-categories-section">
      <div class="ref-wrap festival-categories-intro">
        {heading('EXPLORE OUR FESTIVAL CATEGORIES')}
        <p>From music and food to cultural celebrations and community events,<br class="festival-desktop-break"> ImpactAir puts your brand in the center of the action.</p>
      </div>
      {category_cards()}
    </section>
    <section class="festival-other-types" aria-labelledby="other-types-heading">
      <h2 class="ref-title" id="other-types-heading">OTHER<br>POPULAR<br>FESTIVAL TYPES</h2>
      <div>{''.join(f'<a href="contact.html?interest={key}#quote">{icon(symbol)}<span>{label}</span></a>' for symbol,label,key in OTHER_CATEGORIES)}</div>
    </section>
    <section class="festival-multi-campaign">
      {photo('categories', 10, 1276, 1004, 246, 'An IMPACTAIR billboard on a green festival lawn, ready for a summer brand campaign.', 'festival-multi-photo')}
      <div class="festival-multi-copy">
        {heading('ADVERTISE ACROSS<br>MULTIPLE FESTIVALS')}
        <p>Build brand awareness, drive engagement<br>and reach new customers all summer long.</p>
        {button('Request a 2027 Media Proposal', 'contact.html?interest=2027#quote')}
      </div>
    </section>
  </div>
</div>
'''


FESTIVAL_REFERENCE = {
    'festivals.html': page('Why Festivals?', 'Discover the festival advantage: large audiences, high engagement and standout brand visibility across Ontario.', WHY_FESTIVALS),
    '2027-festival-opportunities.html': page('2027 Festival Opportunities', 'Put your brand in front of millions at Ontario’s top festivals and events. Explore featured 2027 festival advertising opportunities.', OPPORTUNITIES_PAGE),
    'festival-categories.html': page('Festival Categories', 'Explore music, food, Caribbean, multicultural and community festival advertising with IMPACTAIR across Ontario.', CATEGORIES_PAGE),
}
