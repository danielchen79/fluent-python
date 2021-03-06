from array import array
from math import atan2, sqrt, pi
import reprlib, numbers
from functools import reduce
from operator import xor
from itertools import chain, zip_longest
import numbers

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        s_index = slice(components.find('['), -1)
        components = components[s_index]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

    def __hash__(self):
        hashes = map(hash, self._components)
        return reduce(xor, hashes, 0)

    def __abs__(self):
        return sqrt(sum( x * x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            pairs = zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __radd__(self, other):
        return self + other

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices mst be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        raise AttributeError('{.__name__!r} object has no attribute {!r}'.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'read-only attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name = cls.__name__, attr_name = name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = sqrt(sum(x * x for x in self[n:]))
        a = atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self._components)))

    def __format__(self, fmt_spec='.5f'):
        if fmt_spec == '':
            fmt_spec = '.3f'
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))


if __name__ == '__main__':
    print('{:*^50}'.format('Unary Operators'))
    v1 = Vector([3, 4, 5])
    print(repr(+v1))
    print(repr(-v1))

    print('{:*^50}'.format('Infix Operators: "+"'))
    v2 = Vector([6, 7, 8])
    print(repr(v1 + v2))
    print(v1 + v2 == Vector([3+6, 4+7, 5+8]))

    v3 = Vector([1, 2])
    print(repr(v1 + v3))

    from vector2d_v3 import Vector2d
    v2d = Vector2d(1, 2)
    print(repr(v1 + v2d))
    print(repr(v2d + v1))
    print(repr(v1 + [1]))
    # print(repr(v1 + 1))
    # print(repr(v1 + 'ABC'))

    print('{:*^50}'.format('Infix Operators: "*"'))
    print(repr(v1 * 10))
    print(repr(11 * v1))
    print(repr(v1 * 10))
    from fractions import Fraction
    print(repr(v1 * Fraction(1, 3)))
    # print(repr(v1 * 'a'))

    print('{:*^50}'.format('Rich Comparison Operators: "=="'))
    va = Vector([1.0, 2.0, 3.0])
    vb = Vector(range(1, 4))
    print(va == vb)
    vc = Vector([1, 2])
    v2d = Vector2d(1, 2)
    print(vc == v2d)
    t3 = (1, 2, 3)
    print(va == t3)
    print(va != vb)
    print(vc != v2d)
    print(va != t3)

    print('{:*^50}'.format('Augmented Assignment Operators: "=="'))
    v1 = Vector([1.0, 2.0, 3.0])
    v1_alias = v1
    print(id(v1))
    v1 += Vector([4, 5, 6])
    print(repr(v1))
    print(id(v1))
    print(repr(v1_alias))
    v1 *= 11
    print(repr(v1))
    print(id(v1))
