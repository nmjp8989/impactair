"""Home and Benefits rebuilt from the supplied desktop compositions."""
from design_common import icon, photo, hero, stats, button, strip, cta


HOME_BODY = '<div class="reference-page home-reference">' + hero(
    'home', 'BIGGER BRANDS.<br>BOLDER EVENTS.<br><em>HIGHER IMPACT.</em>',
    'Inflatable billboard rentals for events,<br>festivals &amp; marketing campaigns.',
    y=54, h=379, cls='home-ref-hero',
    actions=button('Request a Quote','contact.html#quote')+button('Explore Solutions','advertising-solutions.html',True),
) + stats('home-ref-stats') + '''<section class="home-ref-features ref-wrap" aria-label="Why ImpactAir">''' + ''.join(
    f'<article>{icon(i)}<div><h2>{h}</h2><p>{p}</p></div></article>' for i,h,p in [
      ('eye','High Visibility','Giant, attention-grabbing presence.'),
      ('users','Large Audiences','Reach more people at bigger events.'),
      ('calendar','Event Ready','Delivered, set up and taken down for you.'),
      ('layers','Custom Branding','Bold, fully branded designs that get noticed.'),
    ]) + '''</section>
  <section class="home-ref-position"><div class="home-ref-position-inner">
    <div class="home-ref-position-copy"><h2>Advertising That<br>Stands Above<br>the Crowd.</h2><p>Make a bigger impression with inflatable billboard rentals that deliver unmatched visibility at Ontario’s busiest events and spaces.</p></div>''' + photo('home',340,603,684,256,'A Toronto Events inflatable billboard above a festival crowd beside the Toronto skyline','home-ref-position-photo') + '''
  </div></section>
  <section class="home-ref-solutions" id="solutions"><div class="ref-wrap"><h2>Solutions for Every Event</h2><div class="home-ref-solutions-grid">''' + ''.join(
      f'<a class="home-ref-solution" href="{url}">{photo("home",x,933,w,164,alt)}<span>{title}{icon("arrow-right")}</span></a>'
      for x,w,title,url,alt in [
        (31,319,'Festivals &amp; Concerts','festivals.html','An illuminated Music Festival billboard next to a concert stage'),
        (360,310,'Brand Activations','advertising-solutions.html#brand-activations','A branded inflatable billboard at a busy outdoor activation'),
        (678,316,'Corporate Events','advertising-solutions.html#corporate-events','A blue conference billboard at a corporate event'),
      ]) + '''</div></div></section>
  <section class="home-ref-process"><div class="ref-wrap"><h2>How It Works</h2><ol>''' + ''.join(
    f'<li><span class="home-ref-step-icon">{icon(i)}</span><div><h3><span>{n}</span> {title}</h3><p>{copy}</p></div>{icon("arrow-right") if n<3 else ""}</li>'
    for n,i,title,copy in [
      (1,'calendar','Plan','Tell us about your event, location and goals.'),
      (2,'pencil','Customize','Create a bold inflatable with your brand and message.'),
      (3,'rocket','Launch','We deliver, set up and take down, so you can focus on your event.'),
    ]) + '''</ol></div></section>''' + cta(
      'home','BE PART OF ONTARIO’S<br>BIGGEST EVENTS IN 2027.',
      button('Request a Quote','contact.html#quote'),1304,180,'home-ref-cta',
    ) + '</div>'


BENEFIT_ROWS = [
    ('lightbulb','Illuminated','Can be illuminated at night to reflect a new creative message and keep your brand visible <strong>24/7.</strong>',527,466,497,148,'A brightly illuminated Brand Activation billboard at a night festival'),
    ('eye','High Visibility','Everyone will notice it! We select the best possible location at each festival to position inflatable billboards for maximum exposure.',505,621,519,151,'A Toronto Events inflatable billboard above a daytime festival crowd'),
    ('route','Mobility','Demographically and geographically target your audience at festivals you know they will attend.',500,779,524,149,'An IMPACTAIR inflatable display transported on a truck'),
    ('indoor','Indoor','Great for indoor events such as trade shows, conferences, concerts and sporting events.',496,936,528,144,'An IMPACTAIR Trade Show billboard inside an exhibition hall'),
]

BENEFITS_BODY = '<div class="reference-page benefits-reference">' + hero(
    'benefits','THE BENEFITS OF<br>ADVERTISING<br>WITH <em>IMPACTAIR</em>',
    'Powerful, flexible and high-visibility<br>solutions that put your brand<br>in front of massive audiences.',
    y=54,h=328,cls='benefits-ref-hero',kicker='WHY CHOOSE IMPACTAIR?',
) + '<section class="benefits-ref-band">' + strip([
    ('target','BIG<br>EXPOSURE'),('users','LARGE<br>AUDIENCES'),('pin','PREMIUM<br>LOCATIONS'),('calendar','FLEXIBLE<br>RENTALS'),('growth','MEASURABLE<br>IMPACT')
]) + '</section><section class="benefits-ref-rows" aria-label="Advertising benefits">' + ''.join(
    f'<article class="benefits-ref-row"><div class="benefits-ref-row-inner"><div class="benefits-ref-icon">{icon(i)}</div><div class="benefits-ref-copy"><h2>{title}</h2><p>{copy}</p></div>{photo("benefits",x,y,w,h,alt,"benefits-ref-photo")}</div></article>'
    for i,title,copy,x,y,w,h,alt in BENEFIT_ROWS
) + f'''<article class="benefits-ref-row benefits-ref-size"><div class="benefits-ref-row-inner"><div class="benefits-ref-icon">{icon('expand')}</div><div class="benefits-ref-copy"><h2>Super Size Billboard</h2><p><strong>40 ft × 22 ft</strong> overall, with a large-format canvas that puts your brand above the crowd.</p><a href="artwork-specifications.html">View artwork specifications</a></div><div class="benefits-ref-dimensions" role="img" aria-label="A large inflatable billboard measuring 40 feet wide and 22 feet high overall"><div class="benefits-ref-width"><span>40 FT</span></div>{photo('benefits',603,1128,331,128,'','benefits-ref-size-photo')}<div class="benefits-ref-height"><span>22 FT</span></div></div></div></article>
</section>
<section class="benefits-ref-campaign"><div class="benefits-ref-campaign-label"><strong>2027</strong><span>FESTIVAL<br>CAMPAIGN</span></div>''' + stats() + '''</section>
<section class="benefits-ref-cta"><div class="ref-wrap"><h2>PUT YOUR BRAND IN FRONT OF<br>ONTARIO’S BIGGEST AUDIENCES.</h2><div class="ref-actions">''' + button('Request a Quote','contact.html#quote')+button('Contact Us','contact.html',True) + '''</div></div></section></div>'''


HOME_BENEFITS_REFERENCE = {
    'index.html': {'title':'Inflatable Billboard Advertising in Ontario','description':'Bigger brands. Bolder events. Higher impact. IMPACTAIR inflatable billboard rentals for festivals, events and marketing campaigns across Ontario.','custom_layout':True,'extra_css':'assets/home-benefits-reference.css','body':HOME_BODY},
    'benefits.html': {'title':'The Benefits of Advertising with IMPACTAIR','description':'Illumination, high visibility, mobility, indoor placements and super-size inflatable billboards for Ontario festival advertising.','custom_layout':True,'extra_css':'assets/home-benefits-reference.css','no_footer':True,'body':BENEFITS_BODY},
}
