class Father:
    def run(self):
        print('so fast!!')


class Mother:
    def dive(self):
        print('so deep')


class Son(Father, Mother):
    def jump(self):
        print('so high')

    def dive(self):
        print('so deep, son style')


class Car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f

    def drive(self):
        self.fuel -= 10

    def add_fuel(self, f):
        self.fuel += f

    def show_info(self):
        print('id:', self.id)
        print('fuel:', self.fuel)


class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c

    def add_cargo(self, c):
        self.cargo += c

    def show_info(self):
        super().show_info()
        print('cargo:', self.cargo)


def main():
    s = Son()
    s.run()
    s.jump()
    s.dive()

    c = Car('32러5234', 0)
    c.add_fuel(100)
    c.drive()
    c.show_info()

    t = Truck('42러 5959', 0, 0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info()


main()
