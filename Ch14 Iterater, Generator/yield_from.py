def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

print(list(chain('ABC', range(5))))

def chain2(*iterables):
    for it in iterables:
        yield from it

print(list(chain2('DEF', range(3))))
