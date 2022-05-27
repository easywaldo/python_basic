class Natural:
    def __init__(self, n):
        self.setn(n)

    def getn(self):
        return self.__n

    def setn(self, n):
        if(n < 1):
            self.__n = n
        else:
            self.__n = n

    n = property(getn, setn)


def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.n = n2.n + n3.n
    print(n1.n)

    print(n1.__dict__)
    n1.__dict__['_Natural__n'] = 100
    print(n1.__dict__)
    print(n1.n)


if __name__ == '__main__':
    main()
