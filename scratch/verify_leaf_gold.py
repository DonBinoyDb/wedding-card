import cv2
import numpy as np

tl = cv2.imread('media/scratch-leaf-tl.png', cv2.IMREAD_UNCHANGED)
br = cv2.imread('media/scratch-leaf-br.png', cv2.IMREAD_UNCHANGED)

print("TL shape:", tl.shape)
print("BR shape:", br.shape)

# Let's see what colors are in TL:
# Leaves are burgundy: R around 100..160, G around 20..50, B around 30..60 (in RGB)
# In BGR: B around 30..60, G around 20..50, R around 100..160
# Gold is: B around 100..150, G around 160..200, R around 200..230
# Let's count gold pixels in TL:
is_gold_tl = (tl[:, :, 3] > 100) & (tl[:, :, 2] > 170) & (tl[:, :, 1] > 140) & (tl[:, :, 0] < 150)
print("Gold pixels in TL leaf:", np.sum(is_gold_tl))

is_gold_br = (br[:, :, 3] > 100) & (br[:, :, 2] > 170) & (br[:, :, 1] > 140) & (br[:, :, 0] < 150)
print("Gold pixels in BR leaf:", np.sum(is_gold_br))

