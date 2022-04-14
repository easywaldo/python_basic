# 일급함수(일급 객체)
# 1. 런타임 초기화
# 2. 변수할당
# 3. 함수 인수 전달
# 4. 함수 결과 반환

def factorial(num: int):
    '''
    Factorial Function -> num : int
    '''
    if num == 1:
        return 1

    return num * factorial(num-1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(dir(factorial))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))


print(factorial.__name__)
print(factorial.__code__)

var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher order function)
# map, filter, reduce

print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

print()

# reduce
from functools import reduce
from operator import add
from subprocess import call

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))


# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 작성
# 일반 함수 형태로 리팩터링 권장

print(reduce(lambda x, t: x + t, range(1, 11)))


# callable : 호출 연산자 -> 메서드 형태로 호출가능한지 확인
# 호출가능 확인

print(callable(str), callable(A))
print(callable(list), callable(var_func), callable(factorial), callable(3.14))

from operator import mul
from functools import partial

print(mul(10, 10))


# 인수 고정
five = partial(mul, 5)
print(five(10))
print(five(100))

six = partial(five, 6)
print(six())
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))
