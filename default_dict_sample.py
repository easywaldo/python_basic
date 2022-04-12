from collections import defaultdict

s = 'robbot'
d = {}
for k in s:
    d[k] = d.setdefault(k, 0) + 1

print(d)


s = 'robbot'
d = defaultdict(int)

for k in s:
    d[k] += 1

print(d)
print(d['r'], d['o'], d['b'], d['t'], sep=',')


def ret_zero():
    return 0


d = defaultdict(ret_zero)

d['name']
print(d)

d = defaultdict(lambda: 7)
d['age']

print(d)
