import subprocess

script = '''
const el = document.getElementById("couple");
const fam = document.querySelector(".fam-card");
const knot = document.querySelector(".fam-knot");
const amp = document.querySelector(".fam-knot__amp");
console.log("COUPLE_RECT:" + JSON.stringify(el.getBoundingClientRect()));
console.log("FAM_RECT:" + JSON.stringify(fam.getBoundingClientRect()));
console.log("KNOT_RECT:" + JSON.stringify(knot.getBoundingClientRect()));
console.log("AMP_RECT:" + JSON.stringify(amp.getBoundingClientRect()));
'''

html_path = r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_couple.html'
with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('</body>', f'<script>{script}</script></body>')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(c)

cmd = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,9000',
    '--enable-logging',
    '--v=1',
    f'file:///{html_path}'
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)

