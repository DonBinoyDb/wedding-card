import cv2
import numpy as np

img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_couple_mobile.png')

# The fam-card border is #c59b27 [39, 155, 197] BGR
diff = np.abs(img.astype(int) - np.array([39, 155, 197]))
match = np.all(diff < 40, axis=2)
counts = np.sum(match, axis=1)
candidates = np.where(counts > 80)[0]
# filter candidates Y between 500 and 3000
cands = [y for y in candidates if 500 < y < 3000]
print("Fam-card border candidates:", cands)
if len(cands) >= 2:
    y1 = cands[0] - 10
    y2 = cands[-1] + 10
    crop = img[y1:y2, :]
    cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\fam_card_exact.png', crop)
    print(f"Saved fam_card_exact.png from Y={y1} to {y2}, shape={crop.shape}")

    # Now let's find the & in fam_card_exact.png
    # The & is in the middle Y range of the card
    h, w = crop.shape[:2]
    mid = crop[int(h*0.35):int(h*0.65), :]
    # The & is gold / dark gold
    diff_mid = np.abs(mid.astype(int) - np.array([11, 134, 184]))
    match_mid = np.all(diff_mid < 45, axis=2)
    ys_m, xs_m = np.where(match_mid)
    if len(xs_m):
        print(f"& knot in card: X = {xs_m.min()}..{xs_m.max()}")
        print(f"X center of & knot: {(xs_m.min() + xs_m.max())/2:.1f} (card center: {w/2:.1f})")
