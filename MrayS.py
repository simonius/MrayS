import pickle
import sys
import os
from PIL import Image


opts = []
args = []
pypy = 0

for clarg in sys.argv:
	if (clarg[0] == '-'):
		opts.append(clarg)
	else:
		args.append(clarg)

if (len(args) < 4):
	print("to few arguments")
	quit()

if (len(opts) > 0):
	if (opts[0] == "-pypy"):
		pypy = 1

x = int(args[2])
y = int(args[3])
file = args[1]

if (pypy == 1):
	os.system("pypy render.py " + file + " " + str(x) + " " + str(y))
else:
	os.system("./render.py " + file + " " + str(x) + " " + str(y))

img = Image.new('RGB', (x, y), "black")
pixels = img.load()
pic = pickle.load(open(file + ".MrayS", "rb"))
for y in range(len(pic)):
	for x in range(len(pic[y])):
		clr = (pic[y])[x]
		pixels[x, y] = (clr, clr, clr)

img.save(file + ".jpg")
