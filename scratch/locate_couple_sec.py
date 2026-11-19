import cv2
import numpy as np

img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_couple_mobile.png')
print("Total image shape:", img.shape)

# Let's search for the couple photos: couple/1.jpg or couple/2.jpg
# Or search for the background of couple-sec: #f4e9e1 -> BGR [225, 233, 244]
diff = np.abs(img.astype(int) - np.array([225, 233, 244]))
match = np.all(diff < 20, axis=2)
counts = np.sum(match, axis=1)
candidates = np.where(counts > 200)[0]
print("Couple section candidate rows:", candidates[:10], "...", candidates[-10:] if len(candidates) else "")
if len(candidates):
    y1, y2 = candidates.min(), candidates.max()
    print(f"Couple section Y: {y1} to {y2}")
    crop = img[y1:y2, :]
    cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\couple_sec_crop.png', crop)
    print("Saved couple_sec_crop.png with shape:", crop.shape)

