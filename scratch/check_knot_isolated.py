import cv2
import numpy as np

card = cv2.imread(r'd:\wedding-card\scratch\measured_fam_card.png')
h, w = card.shape[:2]
print(f"Card image size: {w} x {h}")

# The knot is between Groom section (top) and Bride section (bottom)
# Groom is roughly Y=0..240
# Knot is roughly Y=240..340
# Bride is roughly Y=340..580

knot_strip = card[240:340, :]
cv2.imwrite(r'd:\wedding-card\scratch\isolated_knot.png', knot_strip)

diff = np.abs(knot_strip.astype(int) - np.array([11, 134, 184]))
match = np.all(diff < 45, axis=2)
ys, xs = np.where(match)

if len(xs):
    print(f"Isolated knot bounds: X = {xs.min()}..{xs.max()} (width: {xs.max() - xs.min()})")
    knot_cx = (xs.min() + xs.max()) / 2.0
    print(f"Knot center X: {knot_cx:.1f} vs card width: {w} (card center: {w/2.0:.1f})")
    print(f"Offset from card center: {knot_cx - w/2.0:.1f}px")

