# hashtable
# key 에 value 를 저장하는 구조 => __dict__
# 파이썬 엔진이 해쉬 기반으로 구성이 되어있음
# python dict => hash table 의 종류

# 키 값에 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 하는 함수 >> 해쉬 주소 >> key 에 대한 value 참조

# dict구조

print(__builtins__.__dict__)

# hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2))     #  list 는 해쉬연산이 불가능하다

# dict setdefault (권장)
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'))
print(source)


new_dict1 = {}
new_dict2 = {}

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)


new_dict3 = {k: v for k, v in source}
print(new_dict3)
