# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Yggdrasil dashboard theme: CSS, tiny JS, SVG sigils, HTML helpers.

Pure strings, no external assets, nothing phones home. D1 imports this.
Colours live in THEMES once; the CSS and the contrast test both read it.
"""
import html

def _vars(t):
    raise NotImplementedError('TODO: implement')

def esc(s):
    raise NotImplementedError('TODO: implement')

def pill(status):
    raise NotImplementedError('TODO: implement')

def gauge(label, pct, status=..., text=None):
    raise NotImplementedError('TODO: implement')

def chips(links):
    raise NotImplementedError('TODO: implement')

def action_button(panel_id, a):
    raise NotImplementedError('TODO: implement')

def card(p):
    """Render one panel dict (see panel contract) as a card."""
    raise NotImplementedError('TODO: implement')

def nav(panels, current=None):
    """The five top tabs. A panel joins a tab with a "tab" key in its build() dict; the script below maps older panels by id."""
    raise NotImplementedError('TODO: implement')

def tools():
    raise NotImplementedError('TODO: implement')

def strip(status, summary):
    raise NotImplementedError('TODO: implement')

def page(title, body_main, panels=..., status=..., summary=..., current=None):
    """Full HTML document. body_main is inner HTML of <main>."""
    raise NotImplementedError('TODO: implement')
