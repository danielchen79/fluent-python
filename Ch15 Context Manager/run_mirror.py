text = 'abcde'
print(text[::-1])

print('{:*^60}'.format('Class LookingGlass as contextmanager'))
from mirror import LookingGlass
with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
    v = 1/0

print(what)
print('Back to normal')

print('{:*^60}'.format('Manually excute context manager'))
manager = LookingGlass()
print(manager)
monster = manager.__enter__()
print(monster == 'LookingGlass: Rubbish')
print(monster)
print(manager)
manager.__exit__(None, None, None)
print(monster)

print('{:*^60}'.format('Generator function as contextmanager'))
from mirror_gen import looking_glass

with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
    1/0
print(what)
print('Back to normal')
