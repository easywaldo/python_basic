class Robot:
    population = 0
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        Robot.population += 1
    
    def say_hi(self):
        print(f'greetings, my master call me {self.name}.')
    
    def cal_add(self, a, b):
        return a + b
    
    def getAge(self):
        return self.__age
    
    
    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots.")
        print(cls)
        
class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__age = age + 10
    
robot1 = Robot('irobot', 42)
print(robot1.getAge())


robotSiri = Siri('mysiri', 20)



##robot1.age = 10000
print(robotSiri.getAge())