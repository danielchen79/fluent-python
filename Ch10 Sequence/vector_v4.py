from array import array
from math import atan2, sqrt, pi
import reprlib, numbers
from functools import reduce
from operator import xor
from itertools import chain

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
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return reduce(xor, hashes, 0)

    def __abs__(self):
        return sqrt(sum( x * x for x in self))

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
    print('{:*^50}'.format('Constructor'))
    print(repr(Vector([1.1, 2.2, 3.3])))
    print(repr(Vector(range(20))))
    print(Vector(range(10)))

    print('{:*^50}'.format('bytes(), .frombytes()'))
    v1 = Vector(range(7))
    print(bytes(v1))
    v1_clone = Vector.frombytes(bytes(v1))
    print(repr(v1_clone))
    print(v1 == v1_clone)

    print('{:*^50}'.format('abs()'))
    print(abs(v1))

    print('{:*^50}'.format('len(), getitem()'))
    v1 = Vector([3, 4, 5])
    print(len(v1))
    print((v1[0], v1[-1]))
    v7 = Vector(range(7))
    print(repr(v7[1:4]))
    # print(v7['a'])

    print('{:*^50}'.format('getattr()'))
    print(v7.x)
    print(v7.y)
    # print(v7.abc)
    # print(v7.A)
    # v7.x = 10
    # v7.m = 10

    print('{:*^50}'.format('hash()'))
    v1 = Vector([3, 4])
    v2 = Vector([3.1, 4.2])
    v3 = Vector([3, 4, 5])
    v6 = Vector(range(6))
    print((hash(v1), hash(v2), hash(v3), hash(v6)))
    v3_2 = Vector([3, 4, 5])
    v3_3 = Vector([3, 4, 5, 6])
    print(v3 == v3_2)
    print(v3 == v3_3)

    print('{:*^50}'.format('format()'))
    v1 = Vector([1, 1, 1])
    print(v1.angle(0))
    print(v1.angle(1))
    print(v1.angle(2))
    for x in v1._components:
        print('pos:', v1._components.index(x))
    print(v1._components)
    print([i for i in v1.angles()])
    print(format(v1))
    print(format(v1, 'h'))
    print(format(v1, '.3eh'))

    vv = Vector(v1)
    print('vv:', vv)
