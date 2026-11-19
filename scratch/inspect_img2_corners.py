import cv2
import numpy as np

img2 = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795087130023_22f25bc8.jpg')
photo_crop = img2[370:790, 45:635]

# Look at top-left and bottom-right of photo_crop
tl = photo_crop[0:150, 0:150]
br = photo_crop[250:420, 440:590]

cv2.imwrite('scratch/img2_photo_crop_tl.png', tl)
cv2.imwrite('scratch/img2_photo_crop_br.png', br)
print("Saved img2 crops for inspection.")

