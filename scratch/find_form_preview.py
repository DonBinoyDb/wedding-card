import cv2
import numpy as np

img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_wishes_form.png')

# Search for the "Add Your Blessing" form card
# The form card has ivory background #fdf6ee -> BGR [238, 246, 253] and border #8a333f -> BGR [63, 51, 138]
diff = np.abs(img.astype(int) - np.array([63, 51, 138]))
match = np.all(diff < 20, axis=2)
counts = np.sum(match, axis=1)
candidates = np.where(counts > 80)[0]
print("Matching row candidates:", candidates)

# Look for rows > 3000
form_rows = [r for r in candidates if r > 3000]
if form_rows:
    y_start = min(form_rows) - 60
    y_end = max(form_rows) + 500
    crop = img[y_start:y_end, :]
    cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\form_card_preview.png', crop)
    print(f"Saved form_card_preview.png from Y={y_start} to {y_end}, shape: {crop.shape}")

