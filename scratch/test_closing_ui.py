import subprocess, cv2

with open(r'd:\wedding-card\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# remove intro header and force visibility
idx1 = c.find('<header class="intro"')
idx2 = c.find('</header>') + 9
if idx1 != -1 and idx2 != -1:
    c = c[:idx1] + c[idx2:]

c = c.replace('class="is-intro"', '')
c = c.replace('</head>', '<style>.rv { opacity: 1 !important; transform: none !important; }</style></head>')

test_path = r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_closing.html'
with open(test_path, 'w', encoding='utf-8') as f:
    f.write(c)

out_png = r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_closing.png'
cmd = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,9000',
    f'--screenshot={out_png}',
    f'file:///{test_path}'
]
subprocess.run(cmd, check=True)

img = cv2.imread(out_png)
# Closing section is near the bottom
h = img.shape[0]
crop_closing = img[h-1200:h, :]
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\closing_preview.png', crop_closing)
print("Saved closing_preview.png with shape:", crop_closing.shape)

