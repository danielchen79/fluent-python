import itertools

print('{:*^60}'.format('itertools.chain()'))
print(list(itertools.chain('ABC', range(2))))
print(list(itertools.chain(enumerate('ABC'))))

print('{:*^60}'.format('itertools.chain.from_iterable()'))
it = itertools.chain.from_iterable(enumerate('ABC'))
print(next(it))
print(next(it))
print(list(it))

print('{:*^60}'.format('zip()'))
print(list(zip('ABC', range(5))))
print(list(zip('ABC', range(5), [10, 20, 30, 40, 50])))

print('{:*^60}'.format('zip_longest()'))
print(list(itertools.zip_longest('ABC', range(5))))
print(list(itertools.zip_longest('ABC', range(5), fillvalue='N/A')))

print('{:*^60}'.format('itertools.product()'))
print(list(itertools.product('ABC', range(2))))
suits = "heart diamond spade clubs".split()
print(list(itertools.product(suits, "AKQJ")))
print(list(itertools.product('ABC', repeat=1)))
print(list(itertools.product('ABC', repeat=2)))
print(list(itertools.product('ABC', repeat=3)))
rows = itertools.product('ABC', repeat=3)
for row in rows:
    print(row)
