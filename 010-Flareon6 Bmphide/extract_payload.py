from PIL import Image

encrypted_data = []
with Image.open("image3.bmp", "r") as image:
  for column in range(image.width):
    for row in range(image.height):
      red, green, blue = image.getpixel((column, row))

      original_data = (red & 0x7) | ((green & 0x7) << 3) | ((blue & 0x3) << 6)
      encrypted_data.append(original_data)

binary_format = bytearray(encrypted_data)
with open("encrypted-data.bin", "wb") as encrypted:
  encrypted.write(binary_format)
