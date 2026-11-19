import cv2
import numpy as np

# 1. Update media/scratch-leaf-tl.png and media/scratch-leaf-br.png
clean_tl = cv2.imread('scratch/clean_leaf_tl.png', cv2.IMREAD_UNCHANGED)
clean_br = cv2.imread('scratch/clean_leaf_br.png', cv2.IMREAD_UNCHANGED)

cv2.imwrite('media/scratch-leaf-tl.png', clean_tl)
cv2.imwrite('media/scratch-leaf-br.png', clean_br)
print("Updated media/scratch-leaf-tl.png and media/scratch-leaf-br.png with pure burgundy leaves (0 gold).")

# 2. Check media/reveal-photo.png
photo = cv2.imread('media/reveal-photo.png', cv2.IMREAD_UNCHANGED)
# Any gold-colored pixels in photo (especially corners) should be transparent
b = photo[:, :, 0].astype(float)
g = photo[:, :, 1].astype(float)
r = photo[:, :, 2].astype(float)

# Gold detection: R > 170, G > 140, B < 140, and (R - B) > 40
is_gold = (photo[:, :, 3] > 0) & (r > 165) & (g > 135) & (b < 140) & (r - b > 40)
# But wait! The bride/groom attire or lights might have golden sparkles in the center,
# only remove gold if it's near the corners or outside the main photo area!
# Corner mask:
h, w = photo.shape[:2]
corner_mask = np.zeros((h, w), dtype=bool)
corner_mask[0:130, 0:130] = True       # top-left corner
corner_mask[h-130:h, w-140:w] = True   # bottom-right corner

gold_in_corners = is_gold & corner_mask
print(f"Removing {np.sum(gold_in_corners)} stray gold pixels from corners of reveal-photo.png")
photo[gold_in_corners, 3] = 0

cv2.imwrite('media/reveal-photo.png', photo)
print("Saved clean media/reveal-photo.png")

