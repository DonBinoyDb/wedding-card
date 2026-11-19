import subprocess, cv2
import numpy as np

with open(r'd:\wedding-card\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# remove intro header and force visibility
idx1 = c.find('<header class="intro"')
idx2 = c.find('</header>') + 9
if idx1 != -1 and idx2 != -1:
    c = c[:idx1] + c[idx2:]

c = c.replace('class="is-intro"', '')
c = c.replace('</head>', '<style>.rv { opacity: 1 !important; transform: none !important; }</style></head>')

test_path = r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_wishes_form.html'
with open(test_path, 'w', encoding='utf-8') as f:
    f.write(c)

out_png = r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_wishes_form.png'
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
print("Tall screenshot shape:", img.shape)

# Let's locate the wishes section:
# In verify_wishes_form.html, search for the text "Add Your Blessing" or title "Blessings & Wishes"
# Or crop between Y=3000 and Y=4500
crop_wishes = img[2900:4300, :]
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\wishes_section_crop.png', crop_wishes)
print("Saved wishes_section_crop.png with shape:", crop_wishes.shape)

