from PIL import Image

im = Image.open("scratch/chrome_index_screenshot.png")
print("Full screenshot dimensions:", im.size)

# Search for the card or crop lower half where reveal is
w, h = im.size
crop_area = (0, max(0, h - 1200), w, h)
cropped = im.crop(crop_area)
cropped.save("scratch/reveal_preview.png")
print("Saved reveal_preview.png:", cropped.size)

