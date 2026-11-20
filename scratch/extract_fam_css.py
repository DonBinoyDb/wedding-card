import re

with open(r'd:\wedding-card\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract <style>...</style>
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
all_css = '\n'.join(styles)

# Find all selectors mentioning fam-
matches = re.findall(r'([^{}]*fam-[^{}]*\{[^{}]*\})', all_css)
for m in matches:
    print(m.strip())
    print('-'*40)

