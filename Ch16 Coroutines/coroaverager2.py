from collections import namedtuple

Result = namedtuple('Result', 'count average')
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

coro_avg = averager()
print(next(coro_avg))
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(15))
try:
    print(coro_avg.send(None))
except StopIteration as e:
    result = e.value
    print(result)
