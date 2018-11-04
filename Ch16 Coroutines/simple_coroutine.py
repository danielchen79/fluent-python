def simple_coroutine():
    print('{:-<30}>'.format('coroutine started'))
    x = yield
    print('{:-<30}>'.format('coroutine received:' + str(x)))

# print('{:*^30}>'.format('Simple Coroutine'))
# my_co = simple_coroutine()
# print(my_co)
# next(my_co)
# my_co.send(42)

# print('{:*^30}>'.format('Coroutine.send(None)'))
# my_co = simple_coroutine()
# my_co.send(None)
# my_co.send(42)

print('{:*^30}>'.format('Coroutine.send(1996)'))
my_co = simple_coroutine()
my_co.send(1996)
