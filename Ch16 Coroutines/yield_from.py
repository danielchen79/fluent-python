def gen():
    for c in 'ABC':
        yield c
    for i in range(1, 4):
        yield i

print(list(gen()))

def chain(*iterables):
    for it in iterables:
        yield from it

print(list(chain('ABC', range(1, 4))))
