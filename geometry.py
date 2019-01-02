__autor__ = 'Dmitrii Dubrovskii'

from geom2d.point import *

l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]
#l2 = [Point(0, 0), Point(1, 2) Point(2, 1)]
l2 = list(l1)
l2[0] = Point(0, 0)

print(l1 == l2)

l2 = sorted(l1)
print(l1)
print(l2)

#sorted by x
def x(p):
    return p.x

l2 = sorted(l1, key=x)

print(l1)
print(l2)

def y(p):
    return p.y

#sorted by y
l2 = sorted(l1, key=y)

print(l1)
print(l2)

#lambda function (sorted by y) we don`t need in this case common function
l2 = sorted(l1, key=lambda p: p.y)

print(l1)
print(l2)

#sorted by distance (we have distance in point.py)
l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))

print(l1)
print(l2)