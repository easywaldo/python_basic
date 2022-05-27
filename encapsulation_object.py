class Person:
    def __init__(self, n, a):
        self.__name = n
        self.__age = a

    def add_age(self, a):
        if(a < 0):
            print('age error')
        else:
            self.__age += a

    def __str__(self):
        return f'name: {self.__name}, age: {self.__age}'


def main():
    p = Person('Waldo', 42)
    # p.__age += 1
    p.add_age(1)
    print(p)
    print(p.__dict__)
    p.address = "Seoul"
    p.nation = "South Korea"
    print(p)
    print(p.__dict__)

    p.__dict__['first'] = "Python"
    p.__dict__['second'] = "Java"
    print(p)
    print(p.__dict__)

if __name__ == '__main__':
    main()
