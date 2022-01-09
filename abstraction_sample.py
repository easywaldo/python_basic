class Robot:
    population = 0
    def __init__(self, name, code):
        self.name = name
        self.code = code
        Robot.population += 1
    def say_hi(self):
        print(f'greetings, my master call me {self.name}.')
    def cal_add(self, a, b):
        return a + b
    def die(self):
        print(f"{self.name} is being destroyed!")
    def __str__(self):
        return f"{self.name} and {self.code}!!"
    
    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots.")
    
siri = Robot("siri", 124823923)
javis = Robot("javis", 2943848)
bixby = Robot("bixby", 98723912)

print(siri.name)
print(javis.name)
print(siri)


print(siri.__dict__)
print(javis.__dict__)
print(bixby.__dict__)

print(Robot.how_many())

Robot.say_hi(siri)


print(dir(siri))

