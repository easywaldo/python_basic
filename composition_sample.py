
import abc


class Robot(metaclass=abc.ABCMeta):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.name
    
    @property
    def age(self):
        return self.age
    
    @age.setter
    def age(self, ageValue):
        self.age = ageValue
        
    def __say_hi(self):
        print(f"Greetings. my master call me {self.__name}.")
    
    def say(self):
        print('say hi')
        
    def cal_add(self, a, b):
        return a + b + 1


class BixbyCal():
    def __init__(self, name, age):
        self.Robot = Robot(name, age)
    
    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
        

bixBy = BixbyCal('compositionBixby', 7)
print(bixBy.cal_add(10, 10))