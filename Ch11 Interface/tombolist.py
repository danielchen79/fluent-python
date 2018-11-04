from random import randrange
from tombola import Tombola

@Tombola.register
class Tombolist(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop form empty Tombolist')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    tomlist = Tombolist(range(3))
    print(tomlist.loaded())
    print(tomlist.inspect())
    print(tomlist())
    print(tomlist())
    print(tomlist())
    # print(tomlist())
    print(Tombolist.__mro__)
    print(issubclass(Tombolist, Tombola))
    print(isinstance(tomlist, Tombola))
