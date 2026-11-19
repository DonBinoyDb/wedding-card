import cv2
import numpy as np

img = cv2.imread('media/reveal-photo.png', cv2.IMREAD_UNCHANGED)
# Inspect top-left region (x: 0..150, y: 0..150)
tl = img[0:150, 0:150]
# Inspect bottom-right region (x: 440..590, y: 250..420)
br = img[250:420, 440:590]

# Check if there are gold pixels (high R, medium G, low B in BGR -> e.g. B < 150, G > 150, R > 180)
gold_mask_tl = (tl[:, :, 3] > 0) & (tl[:, :, 2] > 160) & (tl[:, :, 1] > 140) & (tl[:, :, 0] < 120)
gold_mask_br = (br[:, :, 3] > 0) & (br[:, :, 2] > 160) & (br[:, :, 1] > 140) & (br[:, :, 0] < 120)

print("Gold pixels in top-left:", np.sum(gold_mask_tl))
print("Gold pixels in bottom-right:", np.sum(gold_mask_br))

