import cv2
import numpy as np

img1 = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795086881001_c186c486.jpg')
bg = np.array([238, 246, 253], dtype=float) # cream background in BGR

crop_tl = img1[370:530, 60:220]
crop_br = img1[630:780, 480:630]

# In both crops, we want to extract the burgundy leaf line art.
# The leaf color is burgundy #701d29 -> BGR [41, 29, 112].
# Let's measure distance to burgundy vs distance to background or gold.
burgundy = np.array([41, 29, 112], dtype=float)

# In img1, gold pixels have high green and blue compared to burgundy:
# Gold BGR is roughly [120..150, 180..205, 215..235]
# Cream BGR is [238, 246, 253]
# Burgundy BGR is [41, 29, 112]

# Notice that for burgundy:
# Red component (index 2) is significantly higher than Green (index 1) and Blue (index 0).
# Specifically: R - G > 20 and R - B > 15, and G < 140, B < 140.
# Any gold pixel has G > 160 and B > 100!
# Any cream pixel has G > 230 and B > 220!

def extract_clean_leaf(crop):
    b = crop[:, :, 0].astype(float)
    g = crop[:, :, 1].astype(float)
    r = crop[:, :, 2].astype(float)

    # Calculate "burgundyness" score
    # High score = pure burgundy line art
    # Zero score = gold foil or cream background
    redness = (r - g) + (r - b)
    # Penalize brightness in green and blue (gold and cream have high G and B)
    score = redness - 0.7 * (g + b) + 120

    # Smooth alpha ramp
    alpha = np.clip((score - 20) / 45.0 * 255.0, 0, 255).astype(np.uint8)

    # Explicitly zero out any pixel that looks like gold or cream
    # Gold has g > 150 and b > 90
    is_gold_or_bg = (g > 145) | (b > 135) | (r > 200)
    alpha[is_gold_or_bg] = 0

    # For the RGB channels, use the clean burgundy color so antialiasing blends perfectly with whatever is behind it
    clean_rgba = np.zeros((crop.shape[0], crop.shape[1], 4), dtype=np.uint8)
    clean_rgba[:, :, 0] = 41   # B
    clean_rgba[:, :, 1] = 29   # G
    clean_rgba[:, :, 2] = 112  # R
    clean_rgba[:, :, 3] = alpha
    return clean_rgba

clean_tl = extract_clean_leaf(crop_tl)
clean_br = extract_clean_leaf(crop_br)

# Check gold pixels in the cleaned versions
is_gold_tl = (clean_tl[:, :, 3] > 0) & (clean_tl[:, :, 2] > 170) & (clean_tl[:, :, 1] > 140)
is_gold_br = (clean_br[:, :, 3] > 0) & (clean_br[:, :, 2] > 170) & (clean_br[:, :, 1] > 140)
print("Gold pixels remaining in clean TL:", np.sum(is_gold_tl))
print("Gold pixels remaining in clean BR:", np.sum(is_gold_br))
print("Total non-transparent pixels TL:", np.sum(clean_tl[:, :, 3] > 0))
print("Total non-transparent pixels BR:", np.sum(clean_br[:, :, 3] > 0))

# Test compositing over the photo to see how clean it is!
photo_crop = cv2.imread('media/reveal-photo.png', cv2.IMREAD_UNCHANGED)
# Place clean_tl and clean_br over photo
test_comp = photo_crop.copy()
# TL at top-left
h_tl, w_tl = clean_tl.shape[:2]
# BR at bottom-right
h_br, w_br = clean_br.shape[:2]

cv2.imwrite('scratch/clean_leaf_tl.png', clean_tl)
cv2.imwrite('scratch/clean_leaf_br.png', clean_br)

