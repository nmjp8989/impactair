"""For Advertising Agencies, recreated from the supplied desktop reference.

The original PNG supplies only photographic scenery. Headlines, copy, service
icons and campaign links remain native, accessible page elements.
"""
from design_common import button, hero, icon, photo


CAMPAIGN_URL = 'contact.html?interest=agency#quote'


def _service(name, title, link=''):
    detail = (f'<a class="agency-ref-spec-link" href="{link}">View Specifications '
              f'{icon("arrow-right")}</a>') if link else ''
    return f'''<article class="agency-ref-service-card">
      {icon(name)}<h3>{title}</h3><span class="agency-ref-service-rule" aria-hidden="true"></span>{detail}
    </article>'''


AGENCY_REFERENCE = {
    'for-advertising-agencies.html': {
        'title': 'For Advertising Agencies',
        'description': 'Inflatable billboards for live agency campaigns. Plan large-format displays, custom branding, multi-event bookings, production, setup and takedown with IMPACTAIR.',
        'custom_layout': True,
        'extra_css': 'assets/agency-reference.css',
        'body': '<div class="reference-page agency-reference-page">'
        + hero(
            'agencies',
            'INFLATABLE<br>BILLBOARDS<br><em>FOR LIVE<br>CAMPAIGNS</em>',
            '',
            y=55,
            h=503,
            cls='agency-ref-hero',
            kicker='FOR ADVERTISING<br>AGENCIES',
            actions=button('Discuss a Client Campaign', CAMPAIGN_URL),
        )
        + f'''<section class="agency-ref-brief" aria-labelledby="agency-brief-title">
          <div class="agency-ref-brief-copy">
            <h2 class="agency-ref-slash" id="agency-brief-title">FROM BRIEF TO<br>EVENT DAY</h2>
            <ul class="agency-ref-checklist">
              <li>Large-format displays</li>
              <li>Flexible rentals and multi-event bookings</li>
              <li>Custom branding and production support</li>
              <li>Launches, roadshows and festival activations</li>
              <li>Logistics, setup and takedown</li>
            </ul>
          </div>
          {photo('agencies',545,579,479,332,'Two agency colleagues reviewing a client campaign on a tablet at an outdoor event.',cls='agency-ref-team-photo')}
        </section>
        <section class="agency-ref-services" aria-label="Agency campaign services">
          {_service('users','BILLBOARD<br>FORMATS','artwork-specifications.html')}
          {_service('growth','ARTWORK &amp;<br>PRODUCTION')}
          {_service('calendar','MULTI-EVENT<br>BOOKINGS')}
          {_service('target','SETUP &amp;<br>TAKEDOWN')}
        </section>
        <section class="agency-ref-cta" aria-labelledby="agency-campaign-title">
          <div class="ref-wrap agency-ref-cta-inner">
            <h2 class="agency-ref-slash" id="agency-campaign-title">LET’S PLAN YOUR<br>NEXT <em>CAMPAIGN</em></h2>
            <div class="agency-ref-cta-action">{button('Discuss a Client Campaign', CAMPAIGN_URL)}<p>Share your event dates, locations, and campaign goals.</p></div>
          </div>
          <svg class="agency-ref-cta-waves" viewBox="0 0 1024 110" preserveAspectRatio="none" aria-hidden="true"><path d="M0 54C284 116 701 101 1024 25V75C660 129 340 116 0 69Z" fill="#ff8700"/><path d="M0 48C298 116 703 76 1024 0V27C702 104 296 126 0 66Z" fill="#00bdef"/></svg>
        </section></div>''',
    },
}
