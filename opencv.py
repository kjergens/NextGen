from PIL import Image

import cv2


image = Image.open("/Users/kjergens/Desktop/problemsolving.jpg")

print(image.format, image.size, image.mode)

image.thumbnail((128, 128), Image.ANTIALIAS)
image.rotate(45)

print(image.getbands())

#image.show()

image.save("/Users/kjergens/Desktop/problemsolving_small.jpg", "JPEG")







