from multiprocessing import Process
import time

class SubProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name
    
    def run(self):
        print(f'[sub] {self.name} start')
        ##time.sleep(5)
        print(f'[sub] {self.name} end')
    
if __name__ == '__main__':
    print('[main] start')
    p = SubProcess(name='start coding')
    p.start()
    p.join()
    print('[main] end')