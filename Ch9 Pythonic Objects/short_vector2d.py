from vector2d_v3 import Vector2d

class ShortVector2d(Vector2d):
    typecode = 'f'

if __name__ == '__main__':
    v1 = Vector2d(1.1, 2.2)
    dumped = bytes(v1)
    print(repr(dumped))
    print(len(dumped))
    v1.typecode = 'f'
    dumpf = bytes(v1)
    print(len(dumpf))
    sv = ShortVector2d(1/11, 1/27)
    print(repr(sv))
    print(len(bytes(sv)))
