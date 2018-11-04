from math import hypot

class Vector:
    '''
    >>> v = Vector(3, 4)
    '''
    def __init__(self, x=0, y=0):
        '''
        >>> v = Vector(3, 4)
        >>> v
        Vector(3, 4)
        '''
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        >>> v = Vector(3, 4)
        >>> v
        Vector(3, 4)
        '''
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        '''
        Absolute value
        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0
        >>> abs(v * 3)
        15.0
        '''
        return hypot(self.x, self.y)

    def __bool__(self):
        '''
        >>> v = Vector(0, 0)
        >>> bool(v)
        False
        >>> v = Vector(1, 2)
        >>> bool(v)
        True
        '''
        return bool(abs(self))

    def __add__(self, other):
        '''
        Addition
        >>> v1 = Vector(2, 4)
        >>> v2 = Vector(2, 1)
        >>> v1 + v2
        Vector(4, 5)
        '''
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        '''
        Multiplication
        >>> v = Vector(3, 4)
        >>> v * 3
        Vector(9, 12)
        >>> v * 5
        Vector(15, 20)
        '''
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    '''

    '''
    import doctest
    doctest.testmod()
