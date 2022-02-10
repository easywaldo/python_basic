import multiprocessing as mp

def sub_process(name):
    print("[sub start]")
    print(name)
    print("[sub end]")


## main process
if __name__ == "__main__":
    print("[main] start")
    p = mp.Process(target=sub_process, args=("start coding",))
    p.start()
    cp = mp.current_process()
    print(f'current process {cp.pid}')
    print("[main end]")