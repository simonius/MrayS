class mesh():
	def __init__(self):
		self.triangles = []

		
	def load_raw(self, file):
		infile = open(file, 'r')
		for line in infile:
			floats = [float(x) for x in line.split()]
			self.triangles.append(triangle(floats))

	def test_collision(self, ray):
		dist = []
		for tr in self.triangles:
			dist.append(tr.test_collision(ray))

		min = 0
		for i in range(len(dist)):
			if (dist[i] > 0 and ((dist[i] < dist[min]) or dist[min] < 0) ):
				min = i
		return dist[min]
		
class triangle():
	def __init__(self, floats = [0,0,0,0,0,0,0,0,0]):
		self.p1 = point(floats[0:3])
		self.p2 = point(floats[3:6])
		self.p3 = point(floats[6:9])

	def test_collision(self, ray):
		tr_plane = plane(self)
		if (tr_plane.h.skalar(ray.direction) == 0):
			return 0

		t = skalarp(tr_plane.d.diff(ray.start), tr_plane.h) / tr_plane.h.skalar(ray.direction)
#		t = (tr_plane.dk-tr_plane.a*ray.start.x - tr_plane.b*ray.start.y - tr_plane.c*ray.start.z)/(tr_plane.a * ray.direction.x + tr_plane.b * ray.direction.y + tr_plane.c * ray.direction.z)

		S = ray.point(t)
		rs = vector(self.p1, S)
		a = vector(self.p1, self.p2)
		b = vector(self.p1, self.p3)
		r = (rs.y*b.x - b.y*rs.x)/(a.y*b.x - a.x*b.y)
		s = (rs.x*a.y - a.x*rs.y)/(b.x*a.y - b.y*a.x)

		tst = a.mult(r)
		tst.add(b.mult(s))
		tst.add(self.p1)
		


		if (s <= 1 and r <= 1 and (r + s) <= 1 and r >= 0 and s >= 0):
			return t
		else:
			return -1


class tripel():
	def __init__(self, floats = [0,0,0]):
		self.x = floats[0]
		self.y = floats[1]
		self.z = floats[2]
		self.cls = tripel

	def add(self, trip):
		self.x = trip.x + self.x
		self.y = trip.y + self.y
		self.z = trip.z + self.z

	def sum(self, trip):
		sum = self.opcls()
		sum.x = trip.x + self.x
		sum.y = trip.y + self.y
		sum.z = trip.z + self.z
		return sum

	def sub(self, trip):
		self.x = self.x - trip.x
		self.y = self.y - trip.y
		self.z = self.z - trip.z

	def diff(self, trip):
		diff = self.opcls()
		diff.x = self.x - trip.x
		diff.y = self.y - trip.y
		diff.z = self.z - trip.z
		return diff

	def abs(self)
		abs = (self.x**2 + self.y**2 + self.z**2)**0.5
		return abs

	def debug_print(self):
		print("Tripel: " + str(self.x)+ ":" + str(self.y)+ ":" + str(self.z))
		

class point(tripel):
	def __init__(self, floats = [0, 0, 0]):
		tripel.__init__(self, floats)
		self.opcls = point
	pass

class vector(tripel):
	def __init__(self, p1 = point(), p2 = point()): #broken
		tripel.__init__(self)
		self.add(p2)  #bloody
		self.sub(p1)
		self.opcls = vector
		
	def kreuz(self, b):
		axb = kreuz(self, b)
		return axb

	def skalar(self, b):
		return skalarp(self, b)

	def mult(self, t):
		vec = vector() 
		vec.x = self.x * t
		vec.y = self.y * t
		vec.z = self.z * t
		return vec

class ray():
	def __init__(self, p1 = point([0,0,0]), p2 = point([0,0,0,])):
		self.start = p1
		self.direction = vector(p1, p2)
		#self.direction.sub(p1)

	def point(self, t):
		return self.start.sum(self.direction.mult(t))

	def debug_print(self):
		print("Ray:")
		self.start.debug_print()
		self.direction.debug_print() 

class plane():
	def __init__(self, triangle):
		self.d = vector(point([0,0,0]),  triangle.p1) # init mit nur p1 falsch
		ab = vector(triangle.p1, triangle.p2)
		ac = vector(triangle.p1, triangle.p3)
		self.h = ab.kreuz(ac)
		self.a = self.d.x
		self.b = self.d.y
		self.c = self.d.z
		self.dk =  skalarp(self.d, self.h) 

def kreuz(a, b):
	axb = vector()
	axb.x = a.y * b.z - a.z * b.y
	axb.y = a.z * b.x - a.x * b.z
	axb.z = a.x * b.y - a.y * b.x
	return axb

def skalarp(a, b):
	asb = vector()
	asb = a.x*b.x+a.y*b.y+a.z*b.z
	return asb

