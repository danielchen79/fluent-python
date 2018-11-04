from array import array
from math import hypot

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        return '{}({!r}, {!r})'.format(type(self).__name__, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes(array('d', self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1
print(x, y)
print(repr(v1))
v1_clone = eval(repr(v1))
print(repr(v1_clone))
print(v1)
print(tuple(v1))
print(v1 == v1_clone)
octets = bytes(v1)
print(octets)
print(abs(v1))
print((bool(v1), bool(Vector2d(0, 0))))
