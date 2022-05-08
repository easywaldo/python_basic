# 코루틴 : 단일(싱글) 스레드 , 스택을 기반으로 동작하는 비동기 작업
# 스레드 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 > 멀티스레드
# yeild, send : 메인 <> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 > 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 > 동시성 프로그래밍
# 코루틴 : 스레드에 비해 오버헤드 감소
# 스레드 : 싱글스레드 , 멀티스레드
# 멀티스레드의 경우 프로그래밍하기 복잡하다. 공유되는 자원 >> 교착상태 발생 가능성 >> 컨텍스트 스위칭 비용 발생 >> 자원소비 가능성 증가


def corotuine1():
    print('>>> corotine started')
    i = yield
    print('>>> corotuine received : {}'.format(i))


# 메인루틴
# 제너레이터 선언
cr1 = corotuine1()

print(cr1, type(cr1))


# yield 지점까지 서브루틴 수행
# next(cr1)
# next(cr1)
# snext(cr1)

# 기본 전달 값 None
# 값 전송
# next(cr1)
# cr1.send(100)


# 잘못 된 사용
# cr1.send(100)


# GEN_CREATED : 처음 대기상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태


def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(x + y))
    z = yield y
    print('>>> coroutine completed : {}'.format(x + y + z))
    t = yield


from inspect import getgeneratorstate


cr2 = coroutine2(10)
print(getgeneratorstate(cr2))
print(next(cr2))
cr2.send(100)
print(getgeneratorstate(cr2))
cr2.send(200)


# python 3.5  
# def >> async, yield >> await 문법 지원



# 코루틴 Ex3
# StopIteration 자동 처리(3.5 > await)
# 중첩 코루틴 처리


def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))


t2 = generator1()
print(list(t2))


print()
print()


def generator2():
    yield from 'AB'
    yield from range(1, 4)


t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))


print(list(t3))
    

