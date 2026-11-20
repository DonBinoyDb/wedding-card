import cv2
import numpy as np

img = cv2.imread(r'd:\wedding-card\scratch\fam_card_zone.png')
# Let's save slices or check what is at X=245
# What is the actual width and position of the fam-card in this screenshot?
# The card has white background: find columns where pixels are white:
white = np.all(img > 240, axis=2)
# Sum per column:
col_white = np.sum(white, axis=0)
white_cols = np.where(col_white > 100)[0]
print(f"White card columns: X = {white_cols.min()} to {white_cols.max()}")
print(f"Card center: {(white_cols.min() + white_cols.max())/2.0:.1f}")

# Find where the & is:
# Search for & inside the card bounds (between Y = 200 and Y = 800)
# Look for the knot line: horizontal line of 1px height, color gold
diff = np.abs(img[200:800, :].astype(int) - np.array([11, 134, 184]))
match = np.all(diff < 40, axis=2)
ys, xs = np.where(match)
if len(xs):
    print(f"Match within Y=200..800: X = {xs.min()}..{xs.max()}, Y = {ys.min()}..{ys.max()}")
    print(f"Knot X center: {(xs.min() + xs.max())/2.0:.1f}")
    # Crop knot area
    y_mid = int((ys.min() + ys.max())/2) + 200
    crop = img[y_mid - 40: y_mid + 40, :]
    cv2.imwrite(r'd:\wedding-card\scratch\knot_actual.png', crop)
    print("Saved knot_actual.png")

