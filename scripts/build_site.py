#!/usr/bin/env python3
"""Generate the static, GitHub Pages-ready ImpactAir website (no dependencies)."""
from pathlib import Path
from html import escape
from hashlib import sha256
import re
import shutil
from main_pages import MAIN_PAGES, icon
from support_pages import SUPPORT_PAGES
from about_reference import ABOUT_REFERENCE
from home_benefits_reference import HOME_BENEFITS_REFERENCE
from festival_reference import FESTIVAL_REFERENCE
from support_reference import SUPPORT_REFERENCE
from agency_reference import AGENCY_REFERENCE

ROOT = Path(__file__).resolve().parents[1]
PAGES = {**MAIN_PAGES, **SUPPORT_PAGES, 'about.html': ABOUT_REFERENCE,
         **HOME_BENEFITS_REFERENCE, **FESTIVAL_REFERENCE, **SUPPORT_REFERENCE, **AGENCY_REFERENCE}
ORIGIN = 'https://nmjp8989.github.io/impactair/'
ABOUT_REVISION = sha256(
    (ROOT/'scripts/about_reference.py').read_bytes()
    + (ROOT/'assets/impactair.css').read_bytes()
    + ((ROOT/ABOUT_REFERENCE['extra_css']).read_bytes() if ABOUT_REFERENCE.get('extra_css') else b'')
).hexdigest()[:12]


def asset_url(path):
    """Changed assets receive a fresh URL instead of reusing cached styling."""
    revision = sha256((ROOT/path).read_bytes()).hexdigest()[:12]
    return f'{path}?v={revision}'


def brand():
    return '<a class="brand" href="index.html" aria-label="IMPACTAIR home"><span class="brand-word" aria-hidden="true">IMPACT<b>AIR</b></span></a>'


def navlink(path, label, current):
    active = ' aria-current="page"' if path == current else ''
    href = f'{path}?v={ABOUT_REVISION}' if path == 'about.html' else path
    return f'<a href="{href}"{active}>{label}</a>'


def header(current):
    solutions = [('benefits.html','Benefits'),('artwork-specifications.html','Artwork Specifications'),('for-advertising-agencies.html','For Advertising Agencies')]
    festivals = [('festivals.html','Why Festivals?'),('festival-categories.html','Festival Categories')]
    extra = [('contact.html','Contact Us'),('careers.html','Careers'),('faq.html','Frequently Asked Questions'),('privacy-policy.html','Privacy Policy'),('terms-of-use.html','Terms of Use')]
    def dropdown(label, items):
        active = ' is-current' if current in [path for path,_ in items] else ''
        return f'<details class="more{active}"><summary>{label} {icon("chevron-down")}</summary><div class="more-panel">'+''.join(navlink(*x,current) for x in items)+'</div></details>'
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner">{brand()}
  <button class="menu-toggle" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="site-nav" hidden>{icon('menu')}{icon('close')}</button>
  <nav class="site-nav" id="site-nav" aria-label="Main navigation">
    {navlink('index.html','Home',current)}{navlink('about.html','About',current)}
    {dropdown('Solutions',solutions)}{dropdown('Festivals',festivals)}
    {dropdown('More',extra)}
    <a class="button nav-quote" href="contact.html#quote">Request a Quote</a>
  </nav>
  <a class="button header-quote" href="contact.html#quote">Request a Quote {icon('arrow-right')}</a>
</div></header>'''


def footer(current):
    links = [('about.html','About'),('careers.html','Careers'),('contact.html','Contact'),('faq.html','FAQ'),('privacy-policy.html','Privacy Policy'),('terms-of-use.html','Terms of Use')]
    return f'''<footer class="site-footer reference-footer"><div class="reference-footer-inner">{brand()}<nav class="reference-footer-nav" aria-label="Footer navigation">{''.join(navlink(*x,current) for x in links)}</nav></div></footer>'''


def hero(data):
    variant = data.get('hero', 'page')
    actions = ''.join(f'<a class="button {kind}" href="{url}">{label}</a>' for label,url,kind in data.get('actions', []))
    photo = variant in ('home','compact','opportunities')
    media = '<div class="hero-media"><img src="assets/hero-festival.webp" srcset="assets/hero-festival-768.webp 768w, assets/hero-festival-1280.webp 1280w, assets/hero-festival.webp 1672w" sizes="(max-width: 700px) 680px, 1100px" width="1672" height="941" alt="A navy IMPACTAIR inflatable billboard above a Toronto festival crowd at sunset" fetchpriority="high" decoding="async"></div>' if photo else ''
    return f'''<section class="ia-hero hero-{variant}">{media}<div class="wrap hero-inner"><div class="hero-copy">
      <p class="eyebrow">{data.get('kicker','')}</p><h1>{data['heading']}</h1><p class="hero-intro">{data['intro']}</p>
      {'<div class="hero-actions">'+actions+'</div>' if actions else ''}
    </div></div></section>'''


def document(path, data):
    title = data['title'] + (' | IMPACTAIR' if not data['title'].endswith('IMPACTAIR') else '')
    extra_head = ''
    if data.get('extra_css'):
        extra_head = f'\n  <link rel="stylesheet" href="{asset_url(data["extra_css"])}">'
    html = f'''<!doctype html>
<html lang="en-CA"><head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#001c3e"><meta name="description" content="{escape(data['description'],quote=True)}">
  <title>{escape(title)}</title><link rel="canonical" href="{ORIGIN}{'' if path == 'index.html' else path}">
  <meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(data['description'],quote=True)}">
  <meta property="og:type" content="website"><meta property="og:image" content="{ORIGIN}assets/hero-festival.webp">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="assets/fonts/impact-display.woff" as="font" type="font/woff" crossorigin>
  <link rel="stylesheet" href="{asset_url('assets/impactair.css')}"><link rel="stylesheet" href="{asset_url('assets/reference-pages.css')}"><script src="{asset_url('assets/impactair.js')}" defer></script>{extra_head}
</head><body class="modern-site page-{path.removesuffix('.html')}">
{header(path)}
<main id="main">{'' if data.get('custom_layout') else hero(data)}{data['body']}</main>
{footer(path)}
</body></html>
'''
    # A hidden mobile line break must still leave a word boundary.
    html = re.sub(r'(?<=\S)(<br\b[^>]*>)', r' \1', html)
    return re.sub(r'[ \t]+\n', '\n', html)


def main():
    for path, data in PAGES.items():
        (ROOT/path).write_text(document(path,data),encoding='utf-8')
    # Old inbound URLs keep working; the new navigation is the default experience.
    for name in ('advertising-solutions.html','billboard-specifications.html','faq.html','festivals-events.html','gallery.html'):
        p = ROOT/name
        if not p.exists():
            continue
        text = p.read_text()
        text = re.sub(r'<a class="skip-link"[^>]*>.*?</header>', header(name), text, flags=re.S)
        text = re.sub(r'<footer class="site-footer[^\"]*">.*?</footer>', footer(name), text, flags=re.S)
        if 'assets/legacy-theme.css' not in text:
            text = text.replace('<link rel="stylesheet" href="assets/site.css">', '<link rel="stylesheet" href="assets/site.css">\n  <link rel="stylesheet" href="assets/legacy-theme.css">')
        text = text.replace('href="assets/logo.webp"','href="assets/favicon.svg"')
        text = re.sub(r'href="assets/legacy-theme.css[^\"]*"', f'href="{asset_url("assets/legacy-theme.css")}"', text)
        text = re.sub(r'\s*<link rel="stylesheet" href="assets/reference-pages.css[^\"]*">', '', text)
        text = text.replace('</head>', f'  <link rel="stylesheet" href="{asset_url("assets/reference-pages.css")}">\n</head>')
        text = re.sub(r'src="assets/site.js[^\"]*"', f'src="{asset_url("assets/site.js")}"', text)
        p.write_text(text)
    # Staging directory is preview-only; GitHub Pages serves the checked-in root.
    dist=ROOT/'dist'
    dist.mkdir(exist_ok=True)
    for path in dist.glob('*.html'):
        if not (ROOT/path.name).exists():
            path.unlink()
    for path in ROOT.glob('*.html'):
        shutil.copy2(path,dist/path.name)
    shutil.copytree(ROOT/'assets',dist/'assets',dirs_exist_ok=True,ignore=shutil.ignore_patterns('source'))
    shutil.copy2(ROOT/'.nojekyll',dist/'.nojekyll')
    print(f'Generated {len(PAGES)} pages. Preview output: {dist}')


if __name__=='__main__':
    main()
