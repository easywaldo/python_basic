class Person:
    def __init__(self, n, a):
        self.__name__ = n
        self.__age__ = a

    def add_age(self, a):
        if(a < 0):
            print('age error')
        else:
            self.__age__ += a

    def __str__(self):
        return f'name: {self.__name__}, age: {self.__age__}'


def main():
    p = Person('Waldo', 42)
    # p.__age += 1
    p.add_age(1)
    print(p)


if __name__ == '__main__':
    main()
