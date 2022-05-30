class Natural:
    def __init__(self, n, z=0):
        self.setn(n)
        self.z = z

    def getn(self):
        return self.__n

    def setn(self, n):
        if(n < 1):
            self.__n = n
        else:
            self.__n = n

    n = property(getn, setn)

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        if (z < 1):
            self.__z = 1
        else:
            self.__z = z


def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3, 1)
    n1.n = n2.n + n3.n
    print(n1.n)

    print(n1.__dict__)
    n1.__dict__['_Natural__n'] = 100
    print(n1.__dict__)
    print(n1.n)

    n3.z = 99
    n3.z += 1
    print(n3.z)


if __name__ == '__main__':
    main()
