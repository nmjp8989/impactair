"""Shared live components for the supplied desktop reference designs."""
from html import escape


def icon(name):
    return f'<svg class="ref-icon" aria-hidden="true" width="48" height="48"><use href="assets/reference-icons.svg#{name}"></use></svg>'


def photo(sheet, x, y, w, h, alt='', cls='', eager=False):
    """Show an original photographic region without resampling its pixels."""
    label = f' role="img" aria-label="{escape(alt, quote=True)}"' if alt else ' aria-hidden="true"'
    loading = 'eager' if eager else 'lazy'
    return (f'<div class="ref-photo {cls}" style="aspect-ratio:{w}/{h}"{label}>'
            f'<img src="assets/references/{sheet}.png" width="1024" height="1536" alt="" '
            f'loading="{loading}" decoding="async" style="width:{102400/w:.8f}%;left:{-100*x/w:.8f}%;top:0;transform:translateY({-100*y/1536:.8f}%)"></div>')


def button(label, href, outline=False):
    return f'<a class="ref-button{" ref-button-outline" if outline else ""}" href="{escape(href, quote=True)}">{label}{icon("arrow-right")}</a>'


def hero(sheet, title, intro, y=54, h=340, cls='', kicker='', actions=''):
    pos = 100*y/(1536-h)
    return f'''<section class="ref-hero {cls}" style="--hero-ratio:{h/1024};--hero-sheet:url('references/{sheet}.png');--hero-size:{153600/h:.8f}%;--hero-y:{pos:.8f}%">
      <div class="ref-hero-art" aria-hidden="true"></div>
      <div class="ref-wrap"><div class="ref-hero-copy">
        {'<div class="ref-kicker">'+kicker+'</div>' if kicker else ''}
        <h1>{title}</h1><p>{intro}</p>
        {'<div class="ref-actions">'+actions+'</div>' if actions else ''}
      </div></div>
    </section>'''


def stats(cls=''):
    return f'''<section class="ref-stats {cls}" aria-label="2027 festival campaign">
      <div class="ref-stats-inner">
        <div class="ref-stat ref-stat-festivals">{icon('calendar')}<div><strong>50</strong><span>FESTIVALS</span></div></div>
        <div class="ref-stat ref-stat-audience">{icon('users')}<div><strong>7 MILLION</strong><span>PEOPLE</span></div></div>
        <div class="ref-stat ref-stat-season">{icon('calendar')}<div><span>JUNE – SEPTEMBER</span><strong>2027</strong></div></div>
      </div>
    </section>'''


def strip(items, cls=''):
    return '<div class="ref-strip '+cls+'">'+''.join(f'<div>{icon(i)}<span>{label}</span></div>' for i,label in items)+'</div>'


def cta(sheet, title, actions, y, h, cls=''):
    pos = 100*y/(1536-h)
    return f'''<section class="ref-cta {cls}" style="--cta-ratio:{h/1024};--cta-sheet:url('references/{sheet}.png');--cta-size:{153600/h:.8f}%;--cta-y:{pos:.8f}%">
      <div class="ref-cta-art" aria-hidden="true"></div><div class="ref-wrap"><div class="ref-cta-copy"><h2>{title}</h2><div class="ref-actions">{actions}</div></div></div>
    </section>'''
