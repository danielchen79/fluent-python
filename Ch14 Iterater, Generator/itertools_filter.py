def vowel(c):
    return c.lower() in 'aeiou'

print('{:*^60}'.format('filter()'))
print(list(filter(vowel, 'Aardvark')))
print(list(filter(lambda c: c.lower() in 'aeiou', 'Aardvark')))

import itertools
print('{:*^60}'.format('itertools.filterfalse()'))
print(list(itertools.filterfalse(vowel, 'Aardvark')))

print('{:*^60}'.format('itertools.dropwhile()'))
print(list(itertools.dropwhile(vowel, 'Aardvark')))

print('{:*^60}'.format('itertools.dropwhile()'))
print(list(itertools.takewhile(vowel, 'Aardvark')))

print('{:*^60}'.format('itertools.compress()'))
print(list(itertools.compress('Aardvark', (1,0,1,1,0,1))))

print('{:*^60}'.format('itertools.islice(, 4)'))
print(list(itertools.islice('Aardvark', 4)))

print('{:*^60}'.format('itertools.islice(, 4, 7)'))
print(list(itertools.islice('Aardvark', 4, 7)))

print('{:*^60}'.format('itertools.islice(, 1, 7, 2)'))
print(list(itertools.islice('Aardvark', 1, 7, 2)))
