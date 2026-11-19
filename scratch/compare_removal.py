import cv2
import numpy as np

user_img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\.user_uploaded\media_1795090622059_a15d8a0b.jpg')
clean_card = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\clean_card_crop.png')

# User image is 481 x 406 or similar
print("user_img shape:", user_img.shape)
print("clean_card shape:", clean_card.shape)

# Let's crop the center photo area from clean_card
# Card is 680 high, photo is roughly from y=160 to 520
clean_photo_area = clean_card[150:550, :]

# Resize user_img to match height of clean_photo_area
h = clean_photo_area.shape[0]
w_user = int(user_img.shape[1] * (h / user_img.shape[0]))
user_resized = cv2.resize(user_img, (w_user, h))

side_by_side = np.hstack([user_resized, clean_photo_area])
cv2.imwrite(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\remove_gold_comparison.png', side_by_side)
print("Saved remove_gold_comparison.png:", side_by_side.shape)

