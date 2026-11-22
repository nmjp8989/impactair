const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const compact = matchMedia('(max-width: 940px)');
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
const more = navigation.querySelector('.more');

function setMenu(expanded) {
  menu.setAttribute('aria-expanded', String(expanded));
  navigation.dataset.collapsed = String(!expanded);
}

function updateNavigation() {
  menu.hidden = !compact.matches;
  more.open = false;
  setMenu(!compact.matches);
}

menu.addEventListener('click', () => {
  setMenu(menu.getAttribute('aria-expanded') !== 'true');
  if (navigation.dataset.collapsed === 'true') more.open = false;
});
compact.addEventListener('change', updateNavigation);
updateNavigation();

document.addEventListener('click', (event) => {
  if (more.open && !more.contains(event.target)) more.open = false;
  if (compact.matches && !navigation.contains(event.target) && !menu.contains(event.target)) setMenu(false);
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

if ('IntersectionObserver' in window && 'animate' in Element.prototype) {
  const revealObserver = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      revealObserver.unobserve(entry.target);
      if (reducedMotion.matches) continue;
      entry.target.animate(
        [{ opacity: 0.55, transform: 'translateY(13px)' }, { opacity: 1, transform: 'translateY(0)' }],
        { duration: 470, easing: 'cubic-bezier(.18,.75,.24,1)' },
      );
    }
  }, { threshold: 0.14 });

  for (const item of document.querySelectorAll('[data-reveal]')) revealObserver.observe(item);
}

const galleryGrid = document.querySelector('#gallery-grid');
if (galleryGrid) {
  const filters = document.querySelector('.filters');
  const morePhotos = document.querySelector('#more-photos');
  const status = document.querySelector('#gallery-status');
  const preview = document.querySelector('#gallery-preview');
  const previewImage = preview.querySelector('img');
  const caption = preview.querySelector('#gallery-caption');
  const photos = [...galleryGrid.querySelectorAll('.gallery-item')];
  const pageSize = 8;
  let filter = 'all';
  let limit = pageSize;

  function updateGallery(announce = false) {
    let matched = 0;
    for (const photo of photos) {
      const matches = filter === 'all' || photo.dataset.category.split(' ').includes(filter);
      if (matches) matched += 1;
      photo.hidden = !matches || matched > limit;
    }
    morePhotos.hidden = matched <= limit;
    if (announce) status.textContent = 'Showing ' + Math.min(limit, matched) + ' of ' + matched + ' gallery photos.';
  }

  filters.hidden = false;
  filters.addEventListener('click', (event) => {
    const selected = event.target.closest('button[data-filter]');
    if (!selected) return;
    filter = selected.dataset.filter;
    limit = pageSize;
    for (const button of filters.querySelectorAll('button')) {
      button.setAttribute('aria-pressed', String(button === selected));
    }
    updateGallery(true);
  });
  morePhotos.addEventListener('click', () => {
    const firstNew = photos.find((photo) => photo.hidden && (filter === 'all' || photo.dataset.category.split(' ').includes(filter)));
    limit += pageSize;
    updateGallery(true);
    firstNew?.querySelector('a').focus();
  });

  if (typeof preview.showModal === 'function') {
    galleryGrid.addEventListener('click', (event) => {
      const link = event.target.closest('a');
      if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      caption.textContent = link.closest('figure').querySelector('figcaption').textContent;
      previewImage.src = link.href;
      preview.showModal();
    });
    preview.querySelector('button').addEventListener('click', () => preview.close());
    preview.addEventListener('click', (event) => {
      if (event.target === preview) preview.close();
    });
  }

  updateGallery();
}

const quoteForm = document.querySelector('form#quote');
quoteForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  const values = new FormData(quoteForm);
  const fields = {
    name: 'Full name',
    company: 'Company / organization',
    email: 'Email',
    phone: 'Phone',
    dates: 'Preferred date(s)',
    project: 'Event / campaign details',
  };
  const lines = Object.entries(fields).flatMap(([key, label]) => {
    const value = values.get(key)?.trim();
    return value ? [label + ': ' + value] : [];
  });
  const email = quoteForm.dataset.email;
  const status = document.querySelector('#quote-status');
  status.textContent = 'Send the draft from your email app. You can also email ' + email + ' directly.';
  location.href = 'mailto:' + email + '?subject=' +
    encodeURIComponent('IMPACTAIR quote request') + '&body=' + encodeURIComponent(lines.join('\n'));
});
