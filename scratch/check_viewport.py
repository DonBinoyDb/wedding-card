import subprocess

script = '''
console.log("VIEWPORT_WIDTH=" + window.innerWidth);
console.log("BODY_WIDTH=" + document.body.clientWidth);
console.log("WRAP_WIDTH=" + document.querySelector('.wrap').clientWidth);
console.log("WRAP_RECT=" + JSON.stringify(document.querySelector('.wrap').getBoundingClientRect()));
console.log("CARD_RECT=" + JSON.stringify(document.querySelector('.fam-card').getBoundingClientRect()));
console.log("AMP_RECT=" + JSON.stringify(document.querySelector('.fam-knot__amp').getBoundingClientRect()));
'''

with open(r'd:\wedding-card\scratch\test_metric.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace script
idx1 = c.find('<script>')
idx2 = c.find('</script>') + 9
c = c[:idx1] + f'<script>{script}</script>' + c[idx2:]

with open(r'd:\wedding-card\scratch\test_metric.html', 'w', encoding='utf-8') as f:
    f.write(c)

cmd = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,1200',
    '--enable-logging',
    '--v=1',
    'file:///d:/wedding-card/scratch/test_metric.html'
]
res = subprocess.run(cmd, capture_output=True, text=True)
for line in res.stderr.splitlines():
    if any(k in line for k in ['VIEWPORT_WIDTH', 'BODY_WIDTH', 'WRAP_WIDTH', 'WRAP_RECT', 'CARD_RECT', 'AMP_RECT']):
        print(line)

