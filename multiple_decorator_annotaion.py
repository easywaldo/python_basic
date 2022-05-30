def deco1(func):
    def inner():
        print('deco1')
        func()
    return inner


def deco2(func):
    def inner():
        print('deco2')
        func()
    return inner


@deco1
@deco2
def simple():
    print('simple')


def main():
    simple()


main()
