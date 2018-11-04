def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

coro_avg = averager()
print(next(coro_avg))
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(5))
print(coro_avg.close())
from inspect import getgeneratorstate
print(getgeneratorstate(coro_avg))
