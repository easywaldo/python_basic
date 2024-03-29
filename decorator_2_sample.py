# 데코레이터

# 사용 시 장점
# 1. 중복제거 , 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 >> 공통 함수
# 3. 조합해서 사용이 용이

# 단점
# 1. 가독성 감소?
# 2. 특정 기능에 한정된 함수는 > 단일함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습
import time


def perf_clock(func):
    
    def perf_clocked(*args):

        # 함수 싲가 시간
        st = time.perf_counter()

        # 함수 실행
        result = func(*args)

        # 함수 종료 시간
        et = time.perf_counter() - st

        # 실행 함수 명
        name = func.__name__

        # 함수 매개변수
        arg_str = ','.join(repr(arg) for arg in args)

        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))

        return result
    return perf_clocked


@perf_clock
def time_func(seconds):
    return time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


time_func(3)
sum_func(100, 200, 300, 400, 500)


# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)
print('-' * 40, 'Called None Decorator -> time func')
print()
none_deco1(1.5)
none_deco2(100, 200, 300, 400, 500)
