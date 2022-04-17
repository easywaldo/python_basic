# 병행성 : 한 컴퓨터가 여러 일을 동시에 수행 > 단일 프로그램 안에서 여러일을 쉽계 해결
# 병렬성 : 여러 컴퓨터가 여러 작업을 동시에 수행 > 속도


# 제너레이터 예제 1
def geneator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B point'
    print('End')


temp = iter(geneator_ex1())
print(temp)

# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in geneator_ex1():
    print(v)

# 제너레이터 예제 2
temp2 = [x * 3 for x in geneator_ex1()]
temp3 = (x * 3 for x in geneator_ex1())
print(temp2)
print(temp3)

for g in temp2:
    print(g)

for g in temp3:
    print(g)

print()
print()



# 제너레이터 중요 함수
# filterfalse, accumulate, chain, product, groupby...
import itertools

gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

print()
print()



# .... 무한하게 실행
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    # print(v)

# 필터 반대
gen3 = itertools.filterfalse(lambda x: x < 3, [1,2,3,4,5,6,7,8,9,10])

for v in gen3:
    print(v)


# 누적합계
gen4 = itertools.accumulate([x for x in range(1, 101)])
for v in gen4:
    print(v)


# 연결 1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))


# 연결 2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))


# 개별 1
gen7 = itertools.product('ABCDE')
print(list(gen7))


# 개별 2 (연산 경우의 수)
gen8 = itertools.product('ABCDE', repeat=4)
print(list(gen8))


# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDDEEEE')
# print(list(gen9))

for chr, group in gen9:
    print(chr, ' : ', list(group))
