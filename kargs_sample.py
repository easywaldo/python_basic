def who(a, b, c):
    print(a, b, c, sep=',')


who(*[1, 2, 3])

who(*(0.1, 0.2, 0.3))

who(*'abc')

d = dict(a = 1, b = 2, c = 3)

who(*d)

who(**d)

who(*(d.items()))


def func(*args):
    print(args)


func()

func(1)

func(1, 2)

func(1, 2, 3)


def func_s(**args):
    print(args)


func_s(a = 1)

func_s(a = 1, b = 2)

func_s(a = 1, b = 2, c = 3)


def func_t(*args1, **args2):
    print(args1)
    print(args2)


func_t()
func_t(1, a = 1)
func_t(1, 2, a = 1, b = 2, c = 3)