import cv2
import numpy as np

knot_img = cv2.imread(r'd:\wedding-card\scratch\knot_actual.png')
print("knot_actual shape:", knot_img.shape)

# Let's inspect where the line and & are in knot_actual.png:
# In knot_actual, find non-white pixels:
non_white = np.where(np.any(knot_img < 240, axis=2))
ys, xs = non_white
print(f"Non-white pixels in knot_actual: X = {xs.min()}..{xs.max()}")
center = (xs.min() + xs.max()) / 2.0
print(f"Center in crop: {center:.1f} vs image width: {knot_img.shape[1]}")

