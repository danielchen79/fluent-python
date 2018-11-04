sample=[5,4,2,8,7,6,3,0,9,1]
import itertools

print('{:*^60}'.format('accumulate()'))
acc = itertools.accumulate(sample)
print(next(acc))
print(next(acc))
print(list(acc))

print('{:*^60}'.format('accumulate(, min)'))
print(list(itertools.accumulate(sample, min)))

print('{:*^60}'.format('accumulate(, max)'))
print(list(itertools.accumulate(sample, max)))

import operator
print('{:*^60}'.format('accumulate(, operator.mul)'))
print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))

print('{:*^60}'.format('enumerate'))
print(list(enumerate('albatroz', 1)))

print('{:*^60}'.format('map'))
print(list(map(operator.mul, range(11), range(11))))
print(list(map(operator.mul, range(11), [2, 4, 8])))
print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))

print('{:*^60}'.format('itertools.starmap()'))
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))
print(list(itertools.starmap(operator.truediv, enumerate(itertools.accumulate(sample), 1))))
print(list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1))))
