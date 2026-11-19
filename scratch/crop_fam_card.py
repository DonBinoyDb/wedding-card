import cv2
import numpy as np

img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\couple_section_mobile.png')

# The fam-card has a white background (#ffffff or rgba(255,255,255,0.96)) with gold border #c59b27
# Let's find white card background rows:
is_white = np.all(img > 245, axis=2)
white_counts = np.sum(is_white, axis=1)
candidates = np.where(white_counts > 250)[0]

print("White card candidate rows:", candidates)
if len(candidates):
    y1, y2 = candidates.min() - 20, candidates.max() + 20
    card_crop = img[y1:y2, :]
    cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\fam_card_mobile.png', card_crop)
    print(f"Saved fam_card_mobile.png from {y1} to {y2}, shape: {card_crop.shape}")

