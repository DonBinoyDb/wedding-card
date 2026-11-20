import cv2
import numpy as np

img = cv2.imread(r'd:\wedding-card\scratch\test_metric.png')
print("Image shape:", img.shape)

# Find fam-card inside test_metric.png:
# Card background is white
white = np.all(img > 240, axis=2)
row_w = np.sum(white, axis=1)
candidates = np.where(row_w > 200)[0]
# Filter out top if any
cands = [y for y in candidates if y > 300]
if cands:
    y1, y2 = min(cands), max(cands)
    card = img[y1:y2, :]
    cv2.imwrite(r'd:\wedding-card\scratch\measured_fam_card.png', card)
    print(f"Card Y: {y1} to {y2}, shape: {card.shape}")

    # Card horizontal bounds:
    col_w = np.sum(white[y1:y2, :], axis=0)
    card_cols = np.where(col_w > (y2 - y1) * 0.5)[0]
    print(f"Card X bounds: {card_cols.min()} to {card_cols.max()} (width {card_cols.max() - card_cols.min()})")
    print(f"Card center X: {(card_cols.min() + card_cols.max())/2.0:.1f} vs Screen center: {img.shape[1]/2.0:.1f}")

    # Now find the knot in the middle of the card
    h = y2 - y1
    mid_strip = card[int(h*0.35):int(h*0.65), :]
    # Knot is gold #b8860b -> BGR [11, 134, 184]
    diff = np.abs(mid_strip.astype(int) - np.array([11, 134, 184]))
    match = np.all(diff < 45, axis=2)
    ys_k, xs_k = np.where(match)
    if len(xs_k):
        print(f"Knot X bounds: {xs_k.min()} to {xs_k.max()}")
        knot_center = (xs_k.min() + xs_k.max()) / 2.0
        print(f"Knot center X: {knot_center:.1f} vs Card center: {(card_cols.min() + card_cols.max())/2.0:.1f} vs Screen center: {img.shape[1]/2.0:.1f}")

