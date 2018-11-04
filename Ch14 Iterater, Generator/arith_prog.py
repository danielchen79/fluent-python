class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

print('{:*^60}'.format('ArithmeticProgression'))
ap = ArithmeticProgression(0, 1, 3)
print(list(ap))
ap = ArithmeticProgression(1, .5, 3)
print(list(ap))
ap = ArithmeticProgression(0, 1/3, 1)
print(list(ap))
from fractions import Fraction
ap = ArithmeticProgression(0, Fraction(1, 3), 1)
print(list(ap))
from decimal import Decimal
ap = ArithmeticProgression(0, Decimal(.1), .3)
print(list(ap))

def arithprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index

print('{:*^60}'.format('arithprog_gen'))
ap = arithprog_gen(0, 1, 3)
print(list(ap))
ap = arithprog_gen(1, .5, 3)
print(list(ap))
ap = arithprog_gen(0, 1/3, 1)
print(list(ap))
from fractions import Fraction
ap = arithprog_gen(0, Fraction(1, 3), 1)
print(list(ap))
from decimal import Decimal
ap = arithprog_gen(0, Decimal(.1), .3)
print(list(ap))

import itertools
gen = itertools.count(1, .5)
print('{:*^60}'.format('itertools.count'))
print(next(gen))
print(next(gen))
print(next(gen))

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print('{:*^60}'.format('itertools.takewhile'))
print(list(gen))

def arithprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    ap_gen = itertools.count(begin, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen

print('{:*^60}'.format('arithprog_gen V3'))
ap = arithprog_gen(0, 1, 3)
print(list(ap))
ap = arithprog_gen(1, .5, 3)
print(list(ap))
ap = arithprog_gen(0, 1/3, 1)
print(list(ap))
from fractions import Fraction
ap = arithprog_gen(0, Fraction(1, 3), 1)
print(list(ap))
from decimal import Decimal
ap = arithprog_gen(0, Decimal(.1), .3)
print(list(ap))
