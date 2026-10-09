from PIL import Image

img = Image.open(r"C:\Users\hp\OneDrive\Pictures\OIP.webp")
img = img.resize((100, 50))
img = img.convert("L")

chars = "@%#*+=-:. "

for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        print(chars[pixel * len(chars) // 256], end="")
    print()