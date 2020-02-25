import numpy as np

data = np.arange(1,101).reshape(10,10)

#apply a mask that will return only the even numbers
mask = data[data%2==0]
print('Even numbers:', mask)

#using np.where() return only numbers that ends with 6
a = np.where(data%10==6)
print('Numbers that ends with 6:', data[a])

#using the operators: % and | mask to only get numbers that are divisible by 3 and numbers begining with 8

b = np.where((data%3==0) & (data//10==8))
print('Numbers that are divisable by 3 and begins with 8:', data[b])