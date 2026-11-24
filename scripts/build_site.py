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

ROOT = Path(__file__).resolve().parents[1]
PAGES = {**MAIN_PAGES, **SUPPORT_PAGES, 'about.html': ABOUT_REFERENCE}
ORIGIN = 'https://nmjp8989.github.io/impactair/'
ABOUT_REVISION = sha256((ROOT/'scripts/about_reference.py').read_bytes() + (ROOT/'assets/impactair.css').read_bytes()).hexdigest()[:12]


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
    primary = [('index.html','Home'),('about.html','About Us'),('benefits.html','Benefits'),('festivals.html','Festivals'),('contact.html','Contact')]
    extra = [('2027-festival-opportunities.html','2027 Opportunities'),('festival-categories.html','Festival Categories'),('artwork-specifications.html','Artwork Specifications'),('careers.html','Careers')]
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner">{brand()}
  <button class="menu-toggle" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="site-nav" hidden>{icon('menu')}{icon('close')}</button>
  <nav class="site-nav" id="site-nav" aria-label="Main navigation">
    {''.join(navlink(*x, current) for x in primary)}
    <details class="more"><summary>Explore {icon('chevron-down')}</summary><div class="more-panel">{''.join(navlink(*x,current) for x in extra)}</div></details>
    <a class="button nav-quote" href="contact.html#quote">Request a Quote</a>
  </nav>
  <a class="button header-quote" href="contact.html#quote">Request a Quote</a>
</div></header>'''


def footer(current):
    explore = [('index.html','Home'),('about.html','About Us'),('benefits.html','Benefits'),('festivals.html','Festivals & Events')]
    resources = [('2027-festival-opportunities.html','2027 Opportunities'),('festival-categories.html','Festival Categories'),('artwork-specifications.html','Artwork Specifications'),('careers.html','Careers'),('contact.html','Contact Us')]
    return f'''<footer class="site-footer"><div class="wrap footer-inner">
  <div class="footer-brand">{brand()}<p>Bigger brands. Bolder events.<br>Higher impact.</p><a class="footer-email" href="mailto:info@impactair.ca">info@impactair.ca</a><p>Toronto &amp; across Ontario</p></div>
  <nav aria-label="Explore ImpactAir"><h2>Explore</h2>{''.join(navlink(*x,current) for x in explore)}</nav>
  <nav aria-label="Planning resources"><h2>Plan your impact</h2>{''.join(navlink(*x,current) for x in resources)}</nav>
  <div class="footer-invitation"><p class="eyebrow">Your next big moment</p><h2>Let’s make<br><em>an impact.</em></h2><a class="button" href="contact.html#quote">Get Started</a></div>
</div><div class="wrap footer-bottom"><span>© 2026 IMPACTAIR. All rights reserved.</span><nav aria-label="Legal">{navlink('privacy-policy.html','Privacy Policy',current)}{navlink('terms-of-use.html','Terms of Use',current)}</nav></div></footer>'''


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
  <link rel="stylesheet" href="{asset_url('assets/impactair.css')}"><script src="{asset_url('assets/impactair.js')}" defer></script>{extra_head}
</head><body class="modern-site page-{path.removesuffix('.html')}">
{header(path)}
<main id="main">{'' if data.get('custom_layout') else hero(data)}{data['body']}</main>
{'' if data.get('no_footer') else footer(path)}
</body></html>
'''
    return re.sub(r'[ \t]+\n', '\n', html)


def main():
    for path, data in PAGES.items():
        (ROOT/path).write_text(document(path,data),encoding='utf-8')
    # Old inbound URLs keep working; the new navigation is the default experience.
    for name in ('advertising-solutions.html','billboard-specifications.html','case-studies.html','faq.html','festivals-events.html','for-advertising-agencies.html','gallery.html','rental-options.html'):
        p = ROOT/name
        if not p.exists():
            continue
        text = p.read_text()
        text = re.sub(r'<a class="skip-link"[^>]*>.*?</header>', header(name), text, flags=re.S)
        text = re.sub(r'<footer class="site-footer">.*?</footer>', footer(name), text, flags=re.S)
        if 'assets/legacy-theme.css' not in text:
            text = text.replace('<link rel="stylesheet" href="assets/site.css">', '<link rel="stylesheet" href="assets/site.css">\n  <link rel="stylesheet" href="assets/legacy-theme.css">')
        text = text.replace('href="assets/logo.webp"','href="assets/favicon.svg"')
        p.write_text(text)
    # Staging directory is preview-only; GitHub Pages serves the checked-in root.
    dist=ROOT/'dist'
    dist.mkdir(exist_ok=True)
    for path in ROOT.glob('*.html'):
        shutil.copy2(path,dist/path.name)
    shutil.copytree(ROOT/'assets',dist/'assets',dirs_exist_ok=True,ignore=shutil.ignore_patterns('source'))
    shutil.copy2(ROOT/'.nojekyll',dist/'.nojekyll')
    print(f'Generated {len(PAGES)} pages. Preview output: {dist}')


if __name__=='__main__':
    main()
