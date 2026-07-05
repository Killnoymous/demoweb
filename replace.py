import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace demoweb with Quickkfundss
html = re.sub(re.compile('demoweb', re.IGNORECASE), 'Quickkfundss', html)
html = html.replace('demo<span>web</span>', 'Quickk<span>fundss</span>')

# Revert previous demo web replacements if they exist
html = html.replace('demo web', 'Quickkfundss')

# SVG Logo code
svg_logo = '''<svg viewBox="0 0 100 100" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <path d="M 25 85 A 40 40 0 0 0 90 35" fill="none" stroke="#005A9C" stroke-width="8" stroke-linecap="round"/>
  <path d="M 15 65 C 10 40, 25 15, 60 15 L 55 5 L 85 10 L 75 40 L 65 30 C 40 30, 25 45, 25 60 Z" fill="#1CA3D9" />
  <rect x="35" y="55" width="10" height="20" fill="#1CA3D9" />
  <rect x="50" y="40" width="10" height="35" fill="#1CA3D9" />
  <rect x="65" y="25" width="10" height="50" fill="#1CA3D9" />
</svg>'''

# Replace the logo divs
html = re.sub(r'<div class="logo-q">.*?</div>', f'<div class="logo-q" style="background:none;box-shadow:none;">{svg_logo}</div>', html)
html = re.sub(r'<div class="pre-q">.*?</div>', f'<div class="pre-q" style="background:none;box-shadow:none;width:120px;height:120px;">{svg_logo}</div>', html)
html = re.sub(r'<div class="trans-logo">.*?</div>', f'<div class="trans-logo" style="background:none;box-shadow:none;width:100px;height:100px;">{svg_logo}</div>', html)

# Replace the logo text colors to match the brand
html = html.replace('.logo-txt span{color:var(--gold2)}', '.logo-txt{color:#1CA3D9} .logo-txt span{color:#005A9C}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
