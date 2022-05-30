def logger(func):
    def wrapper(arg):
        print("func start")
        func(arg)
        print("func finished")
    return wrapper


@logger
def print_hello(name):
    print(f"hello {name} !!")


print_hello('waldo')
