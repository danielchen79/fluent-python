from array import array

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
mem_oct = memv.cast('B')
print(mem_oct.tolist())
mem_oct[5] = 4
print(numbers)
