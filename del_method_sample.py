
class Car:
    def __init__(self, company, name):
        self.company = company
        self.name = name

    def __del__(self):
        print('deleted')

    def detail(self):
        id_str = id(self)
        print(id_str)


car1 = Car('kia', 'k5')
car1.detail()

del(car1)
car1.detail()
