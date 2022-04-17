from regex import R


c = 300


def func_v3(a):
    global c
    print(a)
    print(c)
    c = 400    


print('>>', c)
func_v3(10)
print('>>>', c)


# closer 사용이유
# 서버프로그래밍 > 동시성 제어 > 메모리 공간에 여러 자원이 접근 > 교착상태
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위함 > Erlang
# 클로저는 공유하되 변경되지 않는 (Immutable, Read Only) 적즉적으로 사용 > 함수형 프로그래밍
# 클로저는 불변자료 구조 및 atom , STM > 멀티스레드 프로그래밍에 강점(코루틴)
# 상태를 기억한다


a = 100

print(a + 100)
print(a + 1000)

# 결과 누적 함수 사용
print(sum(range(1, 51)))
print(sum(range(51, 100)))

# 클래스 이용하는 상태를 기억하는 패턴


class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, v):
        self.series.append(v)
        print('inner >> {} / {}'.format(self.series, len(self.series)))
        return sum(self.series) / len(self.series)


# make instance
average_cls = Averager()

print(average_cls(10))
print(average_cls(20))
print(average_cls(50))
print(average_cls(70))


# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사후 저장 -> 이후에 접근(엑세스) 가능
def closure_ex1():
    series = []
    # 자유 변수
    # 클로저 영역

    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure_1 = closure_ex1()
print(avg_closure_1)
print(avg_closure_1(10))
print(avg_closure_1(30))
print(avg_closure_1(50))
print(avg_closure_1(150))


print()
print()

# function inspection
print(dir(avg_closure_1))
print()
print(dir(avg_closure_1.__code__))
print(avg_closure_1.__code__.co_freevars)
print(avg_closure_1.__closure__[0].cell_contents)


# 잘못된 클로저 사용
def closure_ex2():
    # free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1        # 참조하지 못하는 영역이다
        total += v
        return total / cnt
    return averager

avg_closure_2 = closure_ex2()
# print(avg_closure_2(10))


def closure_ex3():
    # free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total     # cnt, total 이 자유변수가 된다
        cnt += 1        # 참조하지 못하는 영역이다
        total += v
        return total / cnt
    return averager


avg_closure_3 = closure_ex3()
print(avg_closure_3(10))
print(avg_closure_3(30))
print(avg_closure_3(70))


# 함수내에서 값을 변경해서 리턴하는 것은 좋지 않은 디자인이다
# 전역변수는 디버깅하는 경우에도 쉽지 않다


# Outer Function 선언 후 Inner Function Return