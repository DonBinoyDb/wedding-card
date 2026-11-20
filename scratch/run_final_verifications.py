import subprocess, cv2, os
import numpy as np

base_dir = r'd:\wedding-card\scratch'
intro_png = os.path.join(base_dir, 'verify_intro_new.png')
couple_png = os.path.join(base_dir, 'verify_couple_tall.png')

cmd1 = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,850',
    f'--screenshot={intro_png}',
    'file:///d:/wedding-card/index.html'
]
subprocess.run(cmd1, check=True)

im_intro = cv2.imread(intro_png)
print("Intro screenshot shape:", im_intro.shape if im_intro is not None else None)

with open(r'd:\wedding-card\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx1 = c.find('<header class="intro"')
idx2 = c.find('</header>') + 9
if idx1 != -1 and idx2 != -1:
    c = c[:idx1] + c[idx2:]

c = c.replace('class="is-intro"', '')
c = c.replace('</head>', '<style>.rv { opacity: 1 !important; transform: none !important; }</style></head>')

test_path = os.path.join(base_dir, 'verify_couple_check.html')
with open(test_path, 'w', encoding='utf-8') as f:
    f.write(c)

cmd2 = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,9000',
    f'--screenshot={couple_png}',
    f'file:///{test_path}'
]
subprocess.run(cmd2, check=True)

img = cv2.imread(couple_png)
print("Tall couple screenshot shape:", img.shape if img is not None else None)

# In img, let's crop around Y=600 to 1800 to find fam-card
crop_zone = img[600:1800, :]
cv2.imwrite(os.path.join(base_dir, 'fam_card_zone.png'), crop_zone)
print("Saved fam_card_zone.png")

# Search for the golden ampersand #b8860b -> BGR [11, 134, 184]
diff_mid = np.abs(crop_zone.astype(int) - np.array([11, 134, 184]))
match_mid = np.all(diff_mid < 45, axis=2)
ys_m, xs_m = np.where(match_mid)
if len(xs_m):
    # Find the cluster that corresponds to the knot amp
    print(f"Golden pixels in zone: X = {xs_m.min()}..{xs_m.max()}")
    center_x = (xs_m.min() + xs_m.max()) / 2.0
    print(f"Ampersand knot center X: {center_x:.1f} vs image center: {img.shape[1]/2.0:.1f}")
