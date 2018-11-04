from array import array
from math import atan2, sqrt
import reprlib, numbers

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
    
