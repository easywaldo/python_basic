import asyncio
from json.tool import main
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()


# 실행 시작 시간
start = timeit.default_timer()

urls = ['http://slowsplendidyoungplan.neverssl.com/online']


# url open 을 병렬로 실행하기 위한 메서드
async def fetch(url, executor):
    # 스레드명 출력
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    
    # 실행
    response = await loop.run_in_executor(executor, urlopen, url)
    soup = BeautifulSoup(response.read(), 'html.parser')
    
    # 전체 페이지 소스 확인
    print(soup.prettify())
    
    print('Thread Name :', threading.current_thread().getName(), 'Done', url)
    
    # 결과 반환
    return
    # return response.read()[0:10]
    

# 메인 작업 스레드
async def main():
    #  스레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)
    
    # future 객체 모아서 gather 에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    
    # 결과 취합
    rst = await asyncio.gather(*futures)
     
    print()
    print('Result : ', rst)


if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기 
    loop.run_until_complete(main())
    # 수행시간 계산
    duration = timeit.default_timer() - start
    # 총 실행시간
    print('Total Running Time : ', duration)
