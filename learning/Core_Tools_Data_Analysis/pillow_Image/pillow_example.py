from PIL import Image#Standard image (PNG, JPG)

img = Image.open("images/1.jpg")
img.show()

resized = img.resize((100, 100))
resized.show()

gray = img.convert("L")       # Convert to grayscale
rgba = img.convert("RGBA")    # Convert to transparent background
gray.show()

cropped = img.crop((50, 50, 200, 200))  # (left, top, right, bottom)
cropped.show()

cropped.save("images/cropped_version.jpg")

rotated = img.rotate(90)        # Rotate 90 degrees
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
rotated.show()

print(img.format)      # 'JPEG', 'PNG', etc.
print(img.mode)        # 'RGB', 'L' (grayscale), etc.
print(img.size)        # (width, height)