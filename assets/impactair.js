'use strict';

const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const more = navigation?.querySelector('.more');
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
  if (more) more.open = false;
  setMenu(!compact.matches);
}

menu?.addEventListener('click', () => {
  const expanded = menu.getAttribute('aria-expanded') !== 'true';
  setMenu(expanded);
  if (!expanded && more) more.open = false;
});
compact.addEventListener('change', updateNavigation);
updateNavigation();

document.addEventListener('click', (event) => {
  if (more?.open && !more.contains(event.target)) more.open = false;
  if (compact.matches && navigation && menu && !navigation.contains(event.target) && !menu.contains(event.target)) setMenu(false);
});

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  if (more?.open) {
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
    music: 'Music & entertainment festival advertising',
    food: 'Food & culinary festival advertising',
    culture: 'Caribbean & multicultural festival advertising',
    community: 'Community festival advertising',
    'media-proposal': '2027 media proposal',
    'festival-partnership': 'Festival partnership',
  };
  const project = quoteForm.elements.namedItem('project');
  if (topics[interest] && project && !project.value) project.value = 'I’m interested in ' + topics[interest] + '.\n\n';

  quoteForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!quoteForm.reportValidity()) return;
    const values = new FormData(quoteForm);
    const labels = {name:'Full name',company:'Company / organization',email:'Email',phone:'Phone',dates:'Preferred dates',project:'Event / campaign details'};
    const lines = Object.entries(labels).flatMap(([key,label]) => {
      const value = String(values.get(key) || '').trim();
      return value ? [label + ': ' + value] : [];
    });
    const address = quoteForm.dataset.email;
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
