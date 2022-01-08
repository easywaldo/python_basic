class Calculator:
    population = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        Calculator.population += 1

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

cal1 = Calculator(1,2)
cal2 = Calculator(3,4)

print(cal1.a)
print(cal1.b)
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())

print(cal2.a)
print(cal2.b)


cal1.a = 100
print(cal1.a)

print(Calculator.population)