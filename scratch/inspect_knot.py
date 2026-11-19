import cv2
import numpy as np

img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\couple_section_mobile.png')

# In fam-card, find where the golden lines and & are:
# The color of fam-knot is gold #b8860b -> BGR [11, 134, 184]
diff = np.abs(img.astype(int) - np.array([11, 134, 184]))
match = np.all(diff < 40, axis=2)
ys, xs = np.where(match)

if len(xs):
    print(f"Fam knot pixels found: X = {xs.min()}..{xs.max()}, Y = {ys.min()}..{ys.max()}")
    print(f"X center of knot: {(xs.min() + xs.max())/2:.1f} vs image center: {img.shape[1]/2:.1f}")

    # Crop around the knot
    y_center = int((ys.min() + ys.max())/2)
    knot_crop = img[max(0, y_center - 100):min(img.shape[0], y_center + 100), :]
    cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\knot_crop.png', knot_crop)
    print("Saved knot_crop.png")

