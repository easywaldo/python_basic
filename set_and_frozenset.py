from types import MappingProxyType


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



d = {'key': 'value1'}

# read only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정불가
# d_frozen['key2'] = 'value2'

# 수정가능
d['key2'] = 'value2'


s1 = {'apple', 'orange', 'apple', 'orange', 'kiwi'}
s2 = set(['apple', 'orange', 'apple', 'orange', 'kiwi'])
s3 = {3}
s4 = set()
s5 = frozenset({'apple', 'orange', 'apple', 'orange', 'kiwi'})
print(type(s4))

s1.add('melon')
print(s1)

# 추가 불가
# s5.add('melon')


print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

#  선언 최적화
# 바이트 코드 > 파이썬 인터프리터 실행
from dis import dis

print('-----')
print(dis('{10}'))
print('-----')
print(dis('set([10])'))


# 리스트 컴프리헨션
print('-----')
from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})
