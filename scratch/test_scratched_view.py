import subprocess, cv2
import numpy as np

with open(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_production_reveal.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Simulate scratched state by setting canvas opacity to 0 or hidden
c = c.replace('</head>', '<style>#revealCanvas { display: none !important; }</style></head>')

test_scratched_path = r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_scratched.html'
with open(test_scratched_path, 'w', encoding='utf-8') as f:
    f.write(c)

out_png = r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_scratched.png'
cmd = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,9000',
    f'--screenshot={out_png}',
    f'file:///{test_scratched_path}'
]
subprocess.run(cmd, check=True)

img = cv2.imread(out_png)
diff = np.abs(img.astype(int) - np.array([238, 246, 253]))
is_reveal = np.all(diff < 8, axis=2)
ys, xs = np.where(is_reveal)

scratched_crop = img[max(0, ys.min()-40):min(img.shape[0], ys.max()+40), :]
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\scratched_crop.png', scratched_crop)
print('Saved scratched_crop.png with shape:', scratched_crop.shape)

