print("Hello world")
#je suis une catin

from PIL import Image

im = Image.open("Red_square.png")
pix = im.load()
a,b = im.size
pixels = [[pix[i,j] for j in range(a)]for i in range(a)]
print(pixels[0])
print(pixels[1])



