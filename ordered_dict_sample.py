from collections import OrderedDict

d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)

for k, v in d.items():
    print(k, v)

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)

for k, v in od.items():
    print(k, v)

d1 = dict(a=1, b=2, c=3)
d2 = dict(c=3, a=1, b=2)

print(d1)
print(d2)

print(d1 == d2)

od1 = OrderedDict(a=1, b=2, c=3)
od2 = OrderedDict(c=3, b=2, a=1)
print(od1 == od2)


od = OrderedDict(a=1, b=2, c=3)
for kv in od.items():
    print(kv, end=' ')

od.move_to_end('b')
for kv in od.items():
    print(kv, end=' ')

od.move_to_end('b', last=False)
for kv in od.items():
    print(kv, end=' ')
