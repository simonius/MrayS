import poly
import sys
import pickle

if (len(sys.argv) < 4):
	quit()

file = sys.argv[1]
x_pix = int(sys.argv[2])
y_pix = int(sys.argv[3])
meanp = (y_pix * x_pix)**0.5

camerap = poly.point([0.0, 0.0, -10.0])
camerav = poly.vector(poly.point([0, 0, 0]), poly.point([0.0, 0.0, 1.0]))
zoom = 1.0

light1 = (poly.point([0.0, 10, -4]), 200)
lights = [light1]

mesh = poly.mesh()
mesh.load_raw(file)



def calc_pixelpoint(x, y):
	dx = float(x)/meanp - 0.5
	dy = float(y)/meanp - 0.5
	xv = poly.vector(poly.point([0, 0, 0]), poly.point([1, 0, 0]))
	yv = poly.vector(poly.point([0, 0, 0]), poly.point([0, -1, 0]))
	pixel = camerap.sum(camerav.mult(zoom)).sum(xv.mult(dx)).sum(yv.mult(dy))	
	return pixel


def shade(scol, mesh, lights):
	clr = 0
	for light in lights:
		lray = poly.ray(light[0], scol[1])
		lcol = mesh.test_collision(lray)
		if (lcol[0] > 0 and lcol[0] < 0.9999):
			clr = clr + 0.000000001
		else:
			refl = lray.direction.skalar(scol[2].plane.h)/(lray.direction.abs()*scol[2].plane.h.abs())
			clr = clr + light[1] * abs(refl)
	return int(clr)


def render(mesh, x_pix, y_pix):
	x = x_pix
	y = y_pix
	lines = []
	for line_nr in range(y):
		line = []
		for pix in range(x):
			sray = poly.ray(camerap, calc_pixelpoint(pix, line_nr))
			col = mesh.test_collision(sray)
			if (col[0] > 0):
				line.append(shade(col, mesh, lights))
			else:
				line.append(0)
			
		lines.append(line)
	return lines

pic = render(mesh, x_pix, y_pix)
for y in range(len(pic)):
	for x in range(len(pic[y])):
		clr = (pic[y])[x]

pickle.dump(pic, open(file+".MrayS", "wb"))
