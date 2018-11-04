from array import array
from math import atan2, sqrt
import reprlib

class Vector:
    typecode = 'd'

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
        return tuple(self) == tuple(other)

    def __abs__(self):
        return sqrt(sum( x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def angle(self):
        return atan2(self.y, self.x)

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
