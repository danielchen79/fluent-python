import itertools

print('{:*^60}'.format('all(), any()'))
print(all([1, 2, 3]))
print(all([1, 0, 3]))
print(all([]))

print(any([1, 2, 3]))
print(any([1, 0, 0]))
print(any([]))

g = (n for n in [0, 0.0, 7, 8])
print(any(g))
print(next(g))


from random import randint
print('{:*^60}'.format('()'))
def d6():
    return randint(1, 6)

d6_iter = iter(d6, 1)
print(d6_iter)

for roll in d6_iter:
    print(roll)
