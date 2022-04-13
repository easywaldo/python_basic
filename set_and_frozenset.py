a = {'a', 'b', 'c', 'd', 'f'}
b = {'a', 'b', 'd', 'f', 'g'}

print(a - b)

print(a & b)

print(a | b)

print(a ^ b)


a = set(['a', 'c', 'd', 'f'])
b = set(['fdca'])

print(a)
print(b)

print(a == b)
print('a' in a)
print('b' not in a)
for c in a & b:
    print(c, end=' ')


test = set()
test.add(10)
test.add(20)
print(test)


a = frozenset([1,2,3,4,5])
b = frozenset([3,4,5])

print(a - b)
print(a | b)
print(a == b)
print(2 in a)
for c in a & b:
    print(c, end=' ')


print('======')
t = [3, 4, 3, 3, 10, 7, 'a', 'b']
t = list(set(t))
print(t)


os = {1, 2, 3, 4, 5}
os.add(10)
os.discard(1)
print(os)
os.update({7, 8, 9})
print(os)
os &= {2, 4, 6, 8}
print(os)
os -= {2, 4}
print(os)
os ^= {1, 3, 6}
print(os)


s1 = {x for x in range(1, 11)}
print(s1)

s2 = {x**2 for x in s1}
print(s2)

s3 = {x for x in s2 if x < 50}
print(s3)
