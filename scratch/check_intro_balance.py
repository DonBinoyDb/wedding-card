import cv2
import numpy as np

img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\intro_screenshot.png')
# Check where the content is vertically:
# Count non-dark-red pixels across vertical rows
# Background is dark red/black (B < 30, G < 20, R < 60)
bg_diff = np.abs(img.astype(int) - np.array([10, 5, 30]))
is_content = np.any(bg_diff > 40, axis=2)
row_counts = np.sum(is_content, axis=1)

content_rows = np.where(row_counts > 10)[0]
if len(content_rows):
    print(f"Content spans vertical range Y = {content_rows.min()} to {content_rows.max()} (total height {img.shape[0]})")
    center = (content_rows.min() + content_rows.max()) / 2
    print(f"Content vertical center: {center:.1f} (viewport center: {img.shape[0]/2:.1f})")

