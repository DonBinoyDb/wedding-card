import cv2
import numpy as np

unscratched = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_production_reveal.png')
scratched = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_scratched.png')

y1, y2 = 2360, 3040

crop_unscratched = unscratched[y1:y2, :]
crop_scratched = scratched[y1:y2, :]

cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\card_unscratched_final.png', crop_unscratched)
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\card_scratched_final.png', crop_scratched)

# Compare with user reference images
ref_unscratched = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795086881001_c186c486.jpg')
ref_scratched = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795087130023_22f25bc8.jpg')

# Scale ref images to match crop height
h = crop_unscratched.shape[0]
w_ref = int(ref_unscratched.shape[1] * (h / ref_unscratched.shape[0]))
ref_u_scaled = cv2.resize(ref_unscratched, (w_ref, h))
ref_s_scaled = cv2.resize(ref_scratched, (w_ref, h))

# 4-panel comparison: [Ref Unscratched, Our Unscratched] | [Ref Scratched, Our Scratched]
grid = np.hstack([ref_u_scaled, crop_unscratched, ref_s_scaled, crop_scratched])
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\four_panel_comparison.png', grid)
print('Saved four_panel_comparison.png with shape:', grid.shape)

