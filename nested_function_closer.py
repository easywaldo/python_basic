def maker(m):
    def inner(n):
        return m * n
    return inner


def main():
    maker()


if __name__ == '__main__':
    f1 = maker(2)
    f2 = maker(3)

    print(f1)
    print(f2)
    print(f1(2))
    print(f2(3))

    print(f1.__closure__[0].cell_contents)
    print(f2.__closure__[0].cell_contents)
