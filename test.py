import poly
m = poly.mesh()
m.load_raw("ball4.raw")
r1 = poly.ray(p1 = poly.point([1, 20, 1]), p2 = poly.point([1, 19, 1]))
print(m.test_collision(r1))
r1.debug_print()
