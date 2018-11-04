my_list = [[1,2,3], [40,50,60], [7,8,9]]

import functools
print(functools.reduce(lambda a,b: a+b, [sub[1] for sub in my_list]))

import numpy as np
my_array = np.array(my_list)
# print(my_array)
print(np.sum(my_array[:,1]))

import operator
print(functools.reduce(operator.add, [sub[1] for sub in my_list], 0))

# my_list = []
print(sum(sub[1] for sub in my_list))
