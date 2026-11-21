const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const compact = matchMedia('(max-width: 940px)');

function setMenu(expanded) {
  menu.setAttribute('aria-expanded', String(expanded));
  navigation.dataset.collapsed = String(!expanded);
}

function updateNavigation() {
  menu.hidden = !compact.matches;
  setMenu(!compact.matches);
}

menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
compact.addEventListener('change', updateNavigation);
updateNavigation();

const more = navigation.querySelector('.more');
document.addEventListener('click', (event) => {
  if (more.open && !more.contains(event.target)) more.open = false;
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  if (more.open) {
    more.open = false;
    more.querySelector('summary').focus();
  } else if (compact.matches && menu.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    menu.focus();
  }
});

const filters = document.querySelector('.filters');
filters?.addEventListener('click', (event) => {
  const selected = event.target.closest('button[data-filter]');
  if (!selected) return;
  for (const button of filters.querySelectorAll('button')) {
    button.setAttribute('aria-pressed', String(button === selected));
  }
  for (const category of document.querySelectorAll('[data-category]')) {
    category.hidden = selected.dataset.filter !== '0' && selected.dataset.filter !== category.dataset.category;
  }
});

const quoteForm = document.querySelector('#quote-form');
quoteForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  const values = new FormData(quoteForm);
  const labels = {
    name: 'Full name', company: 'Company / organization', email: 'Email', phone: 'Phone',
    type: 'Event type', dates: 'Event date(s)', location: 'Event location',
    attendance: 'Estimated attendance', project: 'Project details',
  };
  const content = Object.entries(labels).map(([key, label]) => label + ': ' + values.get(key).trim()).join('\n');
  const status = document.querySelector('#quote-status');
  status.textContent = 'Send the draft from your email app. You can also email ' + quoteForm.dataset.email + ' directly.';
  status.hidden = false;
  location.href = 'mailto:' + quoteForm.dataset.email + '?subject=' +
    encodeURIComponent('ImpactAir quote request') + '&body=' + encodeURIComponent(content);
});
