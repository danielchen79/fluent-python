def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

res1 = [x*3 for x in gen_AB()]
for i in res1:
    print(i)

print('{:*^60}'.format(''))
res2 = (x*3 for x in gen_AB())
for i in res2:
    print(i)

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence():
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

print('{:*^60}'.format(''))
s = Sentence('"The time has come," the Walrus said,')
print(s)

print('{:*^60}'.format(''))
it = iter(s)
print(next(it))
print(next(it))
print(next(it))

print('{:*^60}'.format(''))
it = iter(s)
for word in s:
    print(word)

print('{:*^60}'.format(''))
it = iter(s)
print(list(it))
