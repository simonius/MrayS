import pickle
import sys
import os
from PIL import Image

if (len(sys.argv) < 4):
	quit()

x = int(sys.argv[2])
y = int(sys.argv[3])
file = sys.argv[1]

os.system("pypy render.py " + file + " " + str(x) + " " + str(y))

img = Image.new('RGB', (x, y), "black")
pixels = img.load()
pic = pickle.load(open(file + ".MrayS", "rb"))
for y in range(len(pic)):
	for x in range(len(pic[y])):
		clr = (pic[y])[x]
		pixels[x, y] = (clr, clr, clr)

img.save(file + ".jpg")
