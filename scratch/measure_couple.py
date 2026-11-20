import subprocess, os

test_html = r'''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
'''

with open(r'd:\wedding-card\index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

s_start = orig.find('<style>') + 7
s_end = orig.find('</style>')
css = orig[s_start:s_end]

# Extract couple section
sec_start = orig.find('<section class="sec s-pearl couple-sec"')
sec_end = orig.find('</section>', sec_start) + 10
sec_html = orig[sec_start:sec_end]

test_content = f'''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {{ margin: 0; padding: 0; background: #fff; }}
{css}
.rv {{ opacity: 1 !important; transform: none !important; }}
</style>
</head>
<body>
{sec_html}
<script>
window.onload = function() {{
  const card = document.querySelector('.fam-card');
  const knot = document.querySelector('.fam-knot');
  const amp = document.querySelector('.fam-knot__amp');
  const data = {{
    card: card.getBoundingClientRect(),
    knot: knot.getBoundingClientRect(),
    amp: amp.getBoundingClientRect()
  }};
  const div = document.createElement('div');
  div.id = 'metrics';
  div.innerText = JSON.stringify(data);
  document.body.appendChild(div);
}};
</script>
</body>
</html>'''

with open(r'd:\wedding-card\scratch\test_metric.html', 'w', encoding='utf-8') as f:
    f.write(test_content)

out_png = r'd:\wedding-card\scratch\test_metric.png'
cmd = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,1200',
    f'--screenshot={out_png}',
    'file:///d:/wedding-card/scratch/test_metric.html'
]
subprocess.run(cmd, check=True)
print("Rendered test_metric.png successfully!")

