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
    
    
    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots.")
        print(cls)
    
robot1 = Robot('irobot', 42)
print(robot1.age)

robot1.age = 10000