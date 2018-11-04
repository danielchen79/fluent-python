from array import array
from math import hypot, atan2

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        return '{}({!r}, {!r})'.format(type(self).__name__, *self)

    def __str__(self):
        return str(tuple(self))

    def __format__(self, fmt_spec='.6f'):
        if fmt_spec == '':
            fmt_spec = '.5f'
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array('d', self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return atan2(self.y, self.x)

print('{:*^50}'.format('Vector2d v1'))
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

print('{:*^50}'.format('.frombytes()'))
v1_clone = Vector2d.frombytes(bytes(v1))
print(repr(v1_clone))
print(v1 == v1_clone)

print('{:*^50}'.format('.format()'))
twd = 1/30.084
print(twd)
print(format(twd, '.4f'))
print('1 TWD = {rate:.3f} USD'.format(rate = twd))
print(format(42, 'b'))
print(format(2/3, '.1%'))
print(format(v1))
print(format(v1, '.3f'))
print(format(v1, '.3e'))
print(format(Vector2d(1, 1), 'p'))
print(format(Vector2d(1, 1), '.3ep'))
print(format(Vector2d(1, 1), '.5fp'))
