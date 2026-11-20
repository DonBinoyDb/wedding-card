from PIL import Image

im = Image.open(r'd:\wedding-card\scratch\verify_intro_new.png')
print("Intro screenshot size:", im.size)
# Crop center of intro screenshot to verify intro.jpg is rendered
crop_intro = im.crop((0, 0, im.size[0], im.size[1]))
crop_intro.save(r'd:\wedding-card\scratch\intro_result.png')
print("Saved intro_result.png")

