import subprocess, cv2
import numpy as np

out_png = r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\intro_screenshot.png'
cmd = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,850',
    f'--screenshot={out_png}',
    'file:///d:/wedding-card/index.html'
]
subprocess.run(cmd, check=True)

our_intro = cv2.imread(out_png)
ref_intro = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795094374382_410a5f36.jpg')

print("Our intro shape:", our_intro.shape)
print("Ref intro shape:", ref_intro.shape)

h = our_intro.shape[0]
w_ref = int(ref_intro.shape[1] * (h / ref_intro.shape[0]))
ref_resized = cv2.resize(ref_intro, (w_ref, h))

combo = np.hstack([ref_resized, our_intro])
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\intro_compare.png', combo)
print("Saved intro_compare.png successfully with shape:", combo.shape)

