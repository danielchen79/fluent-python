import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('"The time has come," the Walrus said,')
print('s[0]:', s[0])
print('s[-1]:', s[-1])

for word in s:
    print(word)

print(list(s))

print('len(s):', len(s))


class Foo():
    def __iter__(self):
        pass

from collections import abc
s = Sentence("ABC")
f = Foo()

try:
    i = iter(f)
    print(i)
except Exception:
    print('Not an iterator')

try:
    i = iter(s)
    print(i)
except Exception:
    print('Not an iterator')

print(issubclass(Foo, abc.Iterable))
print(isinstance(f, abc.Iterable))

s3 = Sentence("Pig and Pepper")
it = iter(s3)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))
print(list(it))
print(list(iter(s3)))
