import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence():
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

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
