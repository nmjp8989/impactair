'use strict';

const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const moreMenus = [...(navigation?.querySelectorAll('.more') || [])];
const compact = matchMedia('(max-width: 960px)');

function setMenu(expanded) {
  if (!menu || !navigation) return;
  menu.setAttribute('aria-expanded', String(expanded));
  menu.setAttribute('aria-label', expanded ? 'Close navigation' : 'Open navigation');
  navigation.dataset.collapsed = String(!expanded);
}

function updateNavigation() {
  if (!menu) return;
  menu.hidden = !compact.matches;
  for (const more of moreMenus) more.open = false;
  setMenu(!compact.matches);
}

menu?.addEventListener('click', () => {
  const expanded = menu.getAttribute('aria-expanded') !== 'true';
  setMenu(expanded);
  if (!expanded) for (const more of moreMenus) more.open = false;
});
compact.addEventListener('change', updateNavigation);
updateNavigation();

document.addEventListener('click', (event) => {
  for (const more of moreMenus) {
    if (more.open && !more.contains(event.target)) more.open = false;
  }
  if (compact.matches && navigation && menu && !navigation.contains(event.target) && !menu.contains(event.target)) setMenu(false);
});

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  const more = moreMenus.find(item => item.open);
  if (more) {
    more.open = false;
    more.querySelector('summary').focus();
  } else if (compact.matches && menu?.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    menu.focus();
  }
});

// Preparing an email is deliberately explicit: this static site has no form backend.
const quoteForm = document.querySelector('form#quote');
if (quoteForm) {
  const interest = new URLSearchParams(location.search).get('interest');
  const topics = {
    festivals: 'Festival advertising',
    '2027': '2027 festival campaign',
    'festival-advertising': 'Festival advertising',
    billboards: 'Inflatable billboards',
    'event-branding': 'Event branding',
    'multi-event': 'Multi-event campaigns',
    music: 'Music & entertainment festival advertising',
    food: 'Food & culinary festival advertising',
    culture: 'Caribbean & multicultural festival advertising',
    community: 'Community festival advertising',
    'media-proposal': '2027 media proposal',
    'festival-partnership': 'Festival partnership',
    'festival-list': 'Full 2027 festival list',
    danforth: 'Taste of the Danforth',
    'beaches-jazz': 'Beaches Jazz Fest',
    'toronto-food': 'Toronto Food Festival',
    caribbean: 'Caribbean festivals',
    'arts-culture': 'Arts & culture festivals',
    sports: 'Sports & active living events',
    wellness: 'Health & wellness events',
    family: 'Family & lifestyle events',
    'corporate-events': 'Corporate events',
  };
  const project = quoteForm.elements.namedItem('message') || quoteForm.elements.namedItem('project');
  if (topics[interest] && project && !project.value) project.value = 'I’m interested in ' + topics[interest] + '.\n\n';
  const interestField = quoteForm.elements.namedItem('interest');
  if (topics[interest] && interestField) {
    if (![...interestField.options].some(option => option.value === interest)) {
      interestField.add(new Option(topics[interest], interest));
    }
    interestField.value = interest;
  }

  quoteForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!quoteForm.reportValidity()) return;
    const values = new FormData(quoteForm);
    const labels = {name:'Full name',company:'Company / organization',email:'Email',phone:'Phone',interest:'Interested in','event-date':'Event date / campaign period',message:'Message',dates:'Preferred dates',project:'Event / campaign details'};
    const lines = Object.entries(labels).flatMap(([key,label]) => {
      let value = String(values.get(key) || '').trim();
      if (key === 'interest' && interestField) value = interestField.selectedOptions[0]?.textContent || value;
      return value ? [label + ': ' + value] : [];
    });
    const address = quoteForm.dataset.email || 'info@impactair.ca';
    const draft = 'mailto:' + address + '?subject=' + encodeURIComponent('IMPACTAIR campaign enquiry') + '&body=' + encodeURIComponent(lines.join('\n'));
    const status = document.querySelector('#quote-status');
    status.replaceChildren(document.createTextNode('Your email draft is ready. Review and send it in your email app. If your app did not open, '));
    const retry = document.createElement('a');
    retry.href = draft;
    retry.target = '_blank';
    retry.rel = 'noopener noreferrer';
    retry.textContent = 'open the draft again';
    status.append(retry, document.createTextNode(' or email ' + address + ' directly.'));
    // Keep the visitor’s completed form available if no mail application is configured.
    window.open(draft, '_blank', 'noopener,noreferrer');
  });
}
