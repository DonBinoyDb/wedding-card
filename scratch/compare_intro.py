import cv2
import numpy as np

our_intro = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\intro_screenshot.png')
ref_intro = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795094374382_410a5f36.jpg')

print("Our intro shape:", our_intro.shape)
print("Ref intro shape:", ref_intro.shape)

# Match heights for side by side
h = our_intro.shape[0]
w_ref = int(ref_intro.shape[1] * (h / ref_intro.shape[0]))
ref_resized = cv2.resize(ref_intro, (w_ref, h))

combo = np.hstack([ref_resized, our_intro])
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\intro_compare.png', combo)
print("Saved intro_compare.png successfully with shape:", combo.shape)

