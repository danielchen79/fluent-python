from array import array

class Fake():
    def __init__(self, x):
        self.x = [i for i in x]

    def __iter__(self):
        return iter(self.x)

    def __repr__(self):
        return 'Fake({})'.format(self.x)

    def __pos__(self):
        return Fake(self)

if __name__ == '__main__':
    f = Fake([42])
    print('invocation:', f)
    print('f.x:', f.x)

    for i in f:
        print('iter:', i)

    f2 = Fake(f)
    print('f2:', f2)
    print('f2.x:', f2.x)

    print('+f:', +f)

    g = Fake(range(5))
    print(g)

    g2 = Fake(g)
    print(g2)
