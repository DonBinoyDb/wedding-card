import cv2
import numpy as np

img1 = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795086881001_c186c486.jpg')
img2 = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795087130023_22f25bc8.jpg')

# Let's inspect leaf_tl_crop = img1[370:530, 60:220]
# and leaf_br_crop = img1[630:780, 480:630]
# Also notice in img2: img2 has the exact same leaves, but with the photo underneath instead of foil!
# Even better: In img1, where the leaves don't touch foil, they are on cream background.
# Where leaves touch foil or photo:
# Burgundy leaves color profile:
# In HSV:
# Hue for burgundy / maroon is around 165..180 or 0..15 in OpenCV (which is 0..180)
# Saturation is > 40
# Value (brightness) is < 160 (it's dark reddish/brownish)
# Gold foil has Hue around 18..35 (yellow-gold), Value > 180!

crop_tl = img1[370:530, 60:220]
crop_br = img1[630:780, 480:630]

# Let's convert to HSV
hsv_tl = cv2.cvtColor(crop_tl, cv2.COLOR_BGR2HSV)
hsv_br = cv2.cvtColor(crop_br, cv2.COLOR_BGR2HSV)

# Leaf mask:
# Burgundy leaves are dark red:
# In RGB: (R - G) > 25, (R - B) > 20, R < 175, G < 100, B < 100
b_tl, g_tl, r_tl = crop_tl[:, :, 0].astype(int), crop_tl[:, :, 1].astype(int), crop_tl[:, :, 2].astype(int)
is_burgundy_tl = (r_tl - g_tl > 22) & (r_tl - b_tl > 15) & (g_tl < 130) & (b_tl < 130) & (r_tl < 185)

b_br, g_br, r_br = crop_br[:, :, 0].astype(int), crop_br[:, :, 1].astype(int), crop_br[:, :, 2].astype(int)
is_burgundy_br = (r_br - g_br > 22) & (r_br - b_br > 15) & (g_br < 130) & (b_br < 130) & (r_br < 185)

# Also check antialiasing around edges
# Let's see how many pixels are detected
print("TL burgundy pixels:", np.sum(is_burgundy_tl))
print("BR burgundy pixels:", np.sum(is_burgundy_br))

# Save mask visualization
cv2.imwrite('scratch/mask_tl.png', (is_burgundy_tl * 255).astype(np.uint8))
cv2.imwrite('scratch/mask_br.png', (is_burgundy_br * 255).astype(np.uint8))

