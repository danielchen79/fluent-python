import collections

class Text(collections.UserString):
    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]

if __name__ == '__main__':
    word = Text('forward')
    print(word)
    print(word.split('w'))
    print(list(reversed(word)))
    print(word.reverse())
    print(Text.reverse(Text('backward')))
    print(type(Text.reverse), type(word.reverse))
    print(list(map(Text.reverse, ['rapid', (10, 20, 30), Text('stressed')])))
    print(Text.reverse.__get__(word))
    print(Text.reverse.__get__(None, word))
    print(word.reverse)
    print(repr(word.reverse.__self__))
    print(word.reverse.__func__ is Text.reverse)
