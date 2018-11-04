my_list = ["peach", "candy", "banana"]
for item in my_list:
    if item == 'banana':
        break
else:
    raise ValueError('No banana found')
