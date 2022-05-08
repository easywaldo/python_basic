# Future 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상


# futures : 비동기 실행을 위한 API 를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기호 코드 매우 쉽계 작성 -> Promise 개념


# 2가지 패턴 실습
# 1. 사용법 > map
# 2. 사용법 > wait , as completed

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed
from unittest import result


WORK_LIST = [100, 1000, 100000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수 (제너레이터)


def sum_generator(n):
    return sum(n for n in range(1, n+1))


def main():

    # worker count
    woker = min(10, len(WORK_LIST))

    # 시작 시간
    start_time = time.time()

    # futures
    futures_list = []

    # 결과건수
    # ProcessPoolExcutor
    with ThreadPoolExecutor() as excutor:

        for work in WORK_LIST:
            # futures 반환
            future = excutor.submit(sum_generator, work)
            # schedule
            futures_list.append(future)
            # schedule 확인
            print(f'Scheduled for {work} : {future}')

        # wait 결과 출력
        result = wait(futures_list, timeout=1)

        # 성공
        print(f'Completed Tasks : {result.done}')
        
        # 실패
        print(f'Pending ones after wating for wating time : {str(result.not_done)}')
        
        # 결과 값 출력
        # print([future.result() for future in result.done])


    # 종료 시간
    end_time = time.time() - start_time

    # 최종 결과 출력
    # print(f'result : {list(result)} {end_time} elasped')


if __name__ == '__main__':
    main()

print()