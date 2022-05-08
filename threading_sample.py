import threading

def work():
    print('[sub] start work')
    keyword = input('input keyword >>> ')
    print(f'{keyword} 로 검색을 시작합니다..')
    print('sub end...')
    
    
print("[main] start")

worker = threading.Thread(target=work)
worker.setDaemon(True)
worker.start()

print('main workding')
print('main finished')