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
		for i in len(dist):
			if (dist.[i] > 0 AND dist[i] < dist[min]):
				min = i
		return dist[min]
		
class triangle():
	def __init__(self, floats = [0,0,0,0,0,0,0,0,0]):
		self.p1 = point(floats[0:3])
		self.p2 = point(floats[3:6])
		self.p3 = point(floats[6:9])

	def test_collision(self, ray):
		return 0
		#change

class tripel():
	def __init__(self, floats = [0,0,0]):
		self.x = floats[0]
		self.y = floats[1]
		self.z = floats[2]

	def add(self, trip):
		self.x = trip.x + self.x
		self.y = trip.y + self.y
		self.z = trip.z + self.z

	def sum(self, trip):
		sum = tripel()
		sum.x = trip.x + self.y
		sum.y = trip.y + self.y
		sum.z = trip.z + self.z
		return sum

	def sub(self, trip):
		self.x = self.x - trip.x
		self.y = self.y - trip.y
		self.z = self.z - trip.z

	def diff(self, trip):
		diff = tripel
		diff.x = self.x - trip.x
		diff.y = self.y - trip.y
		diff.z = self.z - trip.z

class point(tripel):
	pass

class vector(tripel):
	def __init__(self, p1 = point(), p2 = point()):
		self = p2.diff(p1)
		
	def kreuz(self, b):
		axb = kreuz(self, b)
		return axb

class ray():
	def __init__(self, p1 = point([0,0,0]), p2 = point([0,0,0,])):
		self.start = p1
		self.direction = vector(p1, p2)

class plane():
	def __init__(self, triangle):
		self.p = triangle.p1
		ab = vector(triangle.p1, triangle.p2)
		ac = vector(triangle.p1, triangle.p3)
		ab

def kreuz(a, b):
	axb = vector()
	axb.x = ay * bz - az * by
	axb.y = az * bx - ax * bz
	axb.z = ax * by - ay * bx
	return axb

