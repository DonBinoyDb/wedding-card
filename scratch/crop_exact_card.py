import cv2
import numpy as np

# Let's locate the card in verify_scratched.png using template matching with card-title-forever.png
img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_scratched.png')
print('Image loaded:', img.shape)

title_tmpl = cv2.imread(r'd:\wedding-card\media\card-title-forever.png', cv2.IMREAD_UNCHANGED)
# Resize title template to rendered size (~260px wide on 412 viewport)
scale = 260.0 / title_tmpl.shape[1]
resized_title = cv2.resize(title_tmpl, (0, 0), fx=scale, fy=scale)
gray_title = cv2.cvtColor(resized_title[:, :, :3], cv2.COLOR_BGR2GRAY)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(gray_img, gray_title, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(f'Matched title at {max_loc} with confidence {max_val:.3f}')

card_top = max(0, max_loc[1] - 80)
card_bottom = min(img.shape[0], card_top + 600)

scratched_card = img[card_top:card_bottom, :]
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\card_revealed_actual.png', scratched_card)
print('Saved card_revealed_actual.png with shape:', scratched_card.shape)

# Let's also create a side-by-side comparison of unscratched vs scratched
unscratched_img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_production_reveal.png')
unscratched_card = unscratched_img[card_top:card_bottom, :]

combo = np.hstack([unscratched_card, scratched_card])
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\both_states_side_by_side.png', combo)
print('Saved both_states_side_by_side.png with shape:', combo.shape)

