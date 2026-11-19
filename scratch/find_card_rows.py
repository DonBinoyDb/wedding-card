from bs4 import BeautifulSoup
import cv2

# Let's inspect card in verify_production_reveal.html
# We can also find the exact location by looking for the border color or card background color
img = cv2.imread(r'C:\Users\donbi\.gemini\antigravity\brain\ecb39014-19fc-4c2d-b998-a1a9776090ef\scratch\verify_production_reveal.png')

# The card border color is burgundy #701d29 -> BGR [41, 29, 112]
burgundy = np.array([41, 29, 112])
diff = np.abs(img.astype(int) - burgundy)
match = np.all(diff < 20, axis=2)
# Look for horizontal border line across at least 200 pixels
row_counts = np.sum(match, axis=1)
candidates = np.where(row_counts > 100)[0]
print("Row candidates with long burgundy lines:", candidates)

