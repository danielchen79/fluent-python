class DemoException(Exception):
    ""

def demo_exc_finally():
    print('{:-<30}>'.format('Coroutine started'))
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('{:-<30}>'.format('DemoException handled. Continuing'))
            else:
                print('{:-<30}>'.format('Coroutine received:' + repr(x)))
    finally:
        print('{:-<30}>'.format('Corountine ending'))

from inspect import getgeneratorstate
exc_coro = demo_exc_finally()
print(next(exc_coro))
print(getgeneratorstate(exc_coro))
print(exc_coro.send(11))
print(exc_coro.send(22))
# print(exc_coro.close())
print(getgeneratorstate(exc_coro))
print(exc_coro.throw(DemoException))
print(getgeneratorstate(exc_coro))
print(exc_coro.throw(ZeroDivisionError))
