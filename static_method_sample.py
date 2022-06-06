class Simple():
    count = 0

    def __init__(self):
        Simple.count += 1

    @staticmethod
    def get_count():
        return Simple.count

    def sm():
        print('this is static method')
    # sm 를 static method 가 될 수 있도록 한다!!
    sm = staticmethod(sm)

    @staticmethod
    def sm2():
        print('this is static method2')

    def sm3():
        print('this is not static method')
        return Simple.count

    @classmethod
    def sm4(cls):
        print('this is class method')
        return cls.count

    @classmethod
    def sm5(cls):
        print('this is class method and initialzing..')
        return cls()


def main():
    Simple.sm()
    s = Simple()
    s.sm()
    Simple.sm2()
    Simple.sm3()
    s.sm2()
    # s.sm3() # error
    s2 = Simple()
    print(s2.get_count())
    print(Simple.get_count())

    # class method
    print(s2.sm4())

    # clsss method
    s2.sm5()
    print(s2.sm4())


main()
