
"""
    Robot 클래스에 대한 주석
"""
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
        print(cls)
    @staticmethod
    def get_common_robot():
        return Robot("common robot", 999)
    def get_instance(self):
        print('get instance')
        print(id(self))
    def __str__(self):
        return f"{self.name} robot!!"
    def __call__(self):
        print("call")
        return f"{self.name} robot!!"
    @staticmethod
    def are_you_robot():
        return "i am robot"
        
        
        
    
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
print(dir(Robot))

print('doc...')
print(Robot.__doc__)
print(Robot.__class__)


commonRobot = Robot.get_common_robot()
print(commonRobot)

commonRobot2 = Robot.get_common_robot()
print(commonRobot2)


print(siri.get_instance())
print(id(siri))

print(siri())


class Siri(Robot):
    population = 0
    def __init__(self, name, code):
        Siri.population += 1
        super().__init__(name, code)
    def say_hi(self):
        print(f'greetings, my master call me {self.name}.')
    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots.")
        print(cls)
        

siri = Siri("andoro", 10000)
print(siri)
print(siri.are_you_robot())
print(Robot.mro())

print(siri.cal_add(100, 200))

siri.say_hi()
Siri.how_many()



print(dir(object))

print(object.__name__)
print(int)
print(int.mro())
print(int.__init__(3.7))
print(int(7.8))

class A:
    pass
class B:
    pass
class C:
    pass
class D(A, B, C):
    pass

print(D.mro())