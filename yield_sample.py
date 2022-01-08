def number_generator():
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10

for num in number_generator():
    print(num)

g = number_generator()
print(g)


g2 = number_generator()
a = next(g)
b = next(g)
print(a, b)