names = ['waldo', 'teddy', 'zed', 'taylor', 'john', 'alice']
names.sort()

dnames = {}
i = 1
for n in names:
    dnames[i] = n
    i += 1
print(dnames)

eo = enumerate(names)
for n in eo:
    print(n)

for n in enumerate(names, 10):
    print(n)

dnames = {k: v for k, v in enumerate(sorted(names), 1)}
print(dnames)