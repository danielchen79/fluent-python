import itertools
import operator

print('{:*^60}'.format('itertools.count()'))
ct = itertools.count()
print(list(itertools.islice(itertools.count(1, .3), 3)))
print(list(itertools.takewhile(lambda n: n<1.9, itertools.count(1, .3))))

print('{:*^60}'.format('itertools.cycle()'))
cy = itertools.cycle('ABC')
print(list(itertools.islice(cy, 7)))

print('{:*^60}'.format('itertools.repeat()'))
rp = itertools.repeat(7)
print(list(itertools.islice(rp, 7)))
print(list(itertools.repeat(8, 4)))
print(list(map(operator.mul, range(11), itertools.repeat(5))))

print('{:*^60}'.format('itertools.combinations()'))
print(list(itertools.combinations('ABC', 1)))
print(list(itertools.combinations('ABC', 2)))
print(list(itertools.combinations('ABC', 3)))
print(list(itertools.combinations_with_replacement('ABC', 2)))

print('{:*^60}'.format('itertools.permutations()'))
print(list(itertools.permutations('ABC', 2)))
