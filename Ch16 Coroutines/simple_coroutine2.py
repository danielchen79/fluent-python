def simple_cor2(a):
    print('{:-<30}>'.format('Started: a = ' +str(a)))
    b = yield a
    print('{:-<30}>'.format('Received: b = ' +str(b)))
    c = yield a + b
    print('{:-<30}>'.format('Received: c = ' +str(c)))

my_co2 = simple_cor2(1)
from inspect import getgeneratorstate
print(getgeneratorstate(my_co2))
print(next(my_co2))
print(getgeneratorstate(my_co2))
print(my_co2.send(2))
try:
    print(my_co2.send(3))
except StopIteration as e:
    print('StopIteration:' + str(e.value))

print(getgeneratorstate(my_co2))
