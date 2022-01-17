class Robot:
    population = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.population += 1
    
    def say_hi(self):
        print(f'greetings, my master call me {self.name}.')
    
    def cal_add(self, a, b):
        return a + b
    
    def getAge(self):
        return self.__age
    
    @property
    def getName(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    # @age.setter
    # def age(self, ageValue):
    #     print(ageValue)
    #     self.__age = ageValue
    
    
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




print(robotSiri.getAge())
print(robotSiri.getName)

robotSiri.age = 9999
print(robotSiri.getAge())