import subprocess

# Update index.html with couple-card flex on mobile
with open(r'd:\wedding-card\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '''    @media (max-width:640px) {
      .couple-gallery {
        gap: 14px
      }'''

replacement = '''    @media (max-width:640px) {
      .couple-gallery {
        gap: 12px;
        width: 100%;
        max-width: 100%;
        box-sizing: border-box;
      }

      .couple-card {
        flex: 1 1 0;
        min-width: 0;
        max-width: 175px;
      }'''

if target in c:
    c = c.replace(target, replacement)
    with open(r'd:\wedding-card\index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced couple-card responsive styles in index.html")
else:
    print("Target not found in index.html")

