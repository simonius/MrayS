import poly
from PIL import Image

file = "monk.raw"
x_pix = 100
y_pix = 100
camerap = poly.point([0.0, 0.0, -10.0])
camerav = poly.vector(poly.point([0, 0, 0]), poly.point([0.0, 0.0, 1.0]))
zoom = 1.0


mesh = poly.mesh()
mesh.load_raw(file)



def calc_pixelpoint(x, y):
	dx = float(x)/x_pix - 0.5
	dy = float(y)/y_pix - 0.5
	xv = poly.vector(poly.point([0, 0, 0]), poly.point([1, 0, 0]))
	yv = poly.vector(poly.point([0, 0, 0]), poly.point([0, 1, 0]))
	pixel = camerap.sum(camerav.mult(zoom)).sum(xv.mult(dx)).sum(yv.mult(dy))	
	return pixel

def render(mesh, x_pix, y_pix):
	x = x_pix
	y = y_pix
	lines = []
	for line_nr in range(y):
		line = []
		for pix in range(x):
			ray = poly.ray(camerap, calc_pixelpoint(pix, line_nr))
			dist = mesh.test_collision(ray)
			
			if (dist > 0 and dist < 100):
				line.append(100)
			else:
				line.append(0)
		lines.append(line)
	return lines

pic = render(mesh, x_pix, y_pix)
img = Image.new('RGB', (x_pix, y_pix), "black")
pixels = img.load()
for y in range(len(pic)):
	for x in range(len(pic[y])):
		clr = (pic[y])[x]
		pixels[x, y] = (clr, clr, clr)

img.show()
img.save(file + ".jpg")
