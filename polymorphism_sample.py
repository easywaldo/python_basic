
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
    
    def say(self):
        print('say hi')
        
class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def say(self):
        print("hello my apple")
        
class SiriKo(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def say(self):
        print("안녕하세요")

class Bixby(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def say(self):
        print("안녕하세요")
        

siri = Siri('siri', 5)
siriKo = SiriKo('siriKo', 3)


##siri.say()
##siriKo.say()

def commonSay(robot : Robot):
    robot.say()
    
commonSay(siri)
commonSay(siriKo)