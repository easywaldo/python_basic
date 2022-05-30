def smile():
    print("^-^")


def confused():
    print("@_@")


def deco(func):
    def df():
        print('emoji')
        func()
        print('emoji')
    return df


smile = deco(smile)
smile()

confused = deco(confused)
confused()


def adder2(n1, n2):
    return n1 + n2


def adder3(n1, n2, n3):
    return n1 + n2 + n3


print(adder2(3, 4))
print(adder3(3, 4, 5))


def adder_deco(func):
    def add(*args):
        print('inner === ')
        print(*args, sep=' + ', end=' ')
        print("= {0}".format(func(*args)))
    return add


adder2 = adder_deco(adder2)
adder3 = adder_deco(adder3)
adder2(2, 3)
adder3(1, 2, 3)


def adder_deco(func):
    def ad(*args):
        print(*args, sep=' + ', end=' ')
        print('= {0}'.format(func(*args)))
    return ad


@adder_deco
def adder2(n1, n2):
    return n1 + n2


@adder_deco
def adder3(n1, n2, n3):
    return n1 + n2 + n3


def main():
    adder2(10, 20)
    adder3(20, 30, 40)


main()
