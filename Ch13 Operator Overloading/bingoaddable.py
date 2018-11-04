import itertools

from tombola import Tombola
from bingo import BingoCage

class AddableBingoCage(BingoCage):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other,inspec()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = 'right operant in += must be {!r} or an iterable'
                raise TypeError(msg.format(self_cls))
            self.load(other_iterable)
            return self

if __name__ == '__main__':
    vowels = 'AEIOU'
    glob = AddableBingoCage(vowels)
    print(glob.inspect())
    print(glob.pick() in vowels)
    print(len(glob.inspect()))

    glob2 = AddableBingoCage('XYZ')
    glob3 = glob + glob2
    print(len(glob3.inspect()))
    # glob + [10, 20]
    glob3 += 'MN'
    print(len(glob3.inspect()))
