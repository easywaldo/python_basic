x = [1,2,3,4,5,6]
y = x
y[2] = 0

print(x)
print(y)

print(id(x))
print(id(y))

x = [1,2,3,4,5,6]
y = x.copy()
y[2] = 0

print(x)
print(y)

print(id(x))
print(id(y))


import copy
x = [[1,2,3,4,5,6], [10, 20, 30, 40, 50, 60, 70]]
y = copy.deepcopy(x)

y[0][1] = 99

print(x)
print(y)

print(id(x))
print(id(y))


a = [[1,2,3,4,5], [10,20,30,40]]
b = a.copy()
b[1][0] = 99


print(a)
print(b)

print(id(a))
print(id(b))
