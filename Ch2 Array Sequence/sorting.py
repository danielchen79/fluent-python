fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, reverse=True, key=len))
print(fruits)
print(fruits.sort())
print(fruits)

nums = [[1,9], [7, 3], [4, 6]]
print(sorted(nums, key=max))
print(sorted(nums, key=min, reverse=True))
