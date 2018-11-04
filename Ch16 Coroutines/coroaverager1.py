from coroutil import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

from inspect import getgeneratorstate
coro_avg = averager()
print(coro_avg)
print(getgeneratorstate(coro_avg))
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))
print(coro_avg.send('spam'))
