from collections import defaultdict


source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}
new_dict3 = defaultdict(list)

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)


for k, v in source:
    
    new_dict3[k].append(v)

print(new_dict3)
