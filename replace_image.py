import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

img_tag = '<img src="logo.jpeg" style="height: 45px; width: auto;" alt="Quickkfundss Logo">'
large_img_tag = '<img src="logo.jpeg" style="height: 80px; width: auto; border-radius: 8px;" alt="Quickkfundss Logo">'
trans_img_tag = '<img src="logo.jpeg" style="height: 60px; width: auto; border-radius: 8px;" alt="Quickkfundss Logo">'

# 1. Navbar and Footer logos
# Original was: <div class="logo-q"...>...</div><div class="logo-txt"...>...</div>
html = re.sub(r'<div class="logo-q".*?</svg></div>\s*<div class="logo-txt".*?</div>', img_tag, html, flags=re.DOTALL)

# 2. Preloader logo
html = re.sub(r'<div class="pre-q".*?</svg></div>\s*<div class="pre-brand">.*?</div>', large_img_tag, html, flags=re.DOTALL)

# 3. Page transition logo
html = re.sub(r'<div class="trans-logo".*?</svg></div>', trans_img_tag, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
