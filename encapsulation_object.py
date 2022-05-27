class Person:
    def __init__(self, n, a):
<<<<<<< HEAD
        self.__name = n
        self.__age = a
=======
        self.__name__ = n
        self.__age__ = a
>>>>>>> 324c1d5119edd4aa6511fc48b564ed481e04062d

    def add_age(self, a):
        if(a < 0):
            print('age error')
        else:
<<<<<<< HEAD
            self.__age += a

    def __str__(self):
        return f'name: {self.__name}, age: {self.__age}'
=======
            self.__age__ += a

    def __str__(self):
        return f'name: {self.__name__}, age: {self.__age__}'
>>>>>>> 324c1d5119edd4aa6511fc48b564ed481e04062d


def main():
    p = Person('Waldo', 42)
    # p.__age += 1
    p.add_age(1)
    print(p)
<<<<<<< HEAD
    print(p.__dict__)
=======
>>>>>>> 324c1d5119edd4aa6511fc48b564ed481e04062d


if __name__ == '__main__':
    main()
