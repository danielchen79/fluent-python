import itertools

print('{:*^60}'.format('itertools.groupby()'))
print(list(itertools.groupby('LLLLAAGGG')))
print(list(itertools.groupby([1,1,1,1,2,2,2,3,3])))
for char, group in itertools.groupby('LLLLAAGGG'):
    print(char, '->', list(group))
for n, group in itertools.groupby([1,1,1,1,2,2,2,3,3]):
    print(n, '->', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(animals)
for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))

for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))

print('{:*^60}'.format('itertools.tee()'))
print(list(itertools.tee('ABC')))
g1, g2 = itertools.tee('ABC')
print(list(zip(*itertools.tee('ABC'))))
