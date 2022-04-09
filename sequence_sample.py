# sequence
# container > list, tuple, collections.deque    (서로 다은 타입을 저장이 가능하다)
# flat > str, bytes, bytearray, array.array, memoryview   (단일 타입만 저장이 가능하다)
# 가변형 > list, bytearray, array.array, memoryview, deque
# 불변형 > tuple, str, bytes
import array

chars = '+_!@#$)&^'
code_list = [c for c in chars]
print(code_list)

code_list = [ord(s) for s in chars if ord(s) > 40]
print(code_list)

code_list2 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list2)



# gnerator
print(dir(chars))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gen_a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print(type(array_g))
print(array_g.tolist())


def list_for():
    r = []
    for i in range(1, 1001):
        r.append(i)
    return r


def gen_for():
    for i in range(1, 1001):
        yield i


g = gen_for()
print(next(g))
print(next(g))

import sys
arr_list = list_for()
print(arr_list)
print(sys.getsizeof(arr_list))

g_list = gen_for()
print(g_list)
print(sys.getsizeof(g_list))
print('변환.....')
print(list(g_list))


mask1 = [['~'] * 3 for _ in range(3)]       # id 값이 서로 다르게 생성
mask2 = [['~'] * 3] * 3                     # id 값이 동일하게 생성
print(mask1)
print(mask2)

mask1[0][1] = 'X'
print(mask1)

mask2[0][1] = 'X'
print(mask2)

print([id(i) for i in mask1])
print([id(i) for i in mask2])
