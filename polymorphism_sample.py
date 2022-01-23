
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
    
    #Private method 의 경우 __ underscore 
    def __say_hi(self):
        print(f"Greetings. my master call me {self.__name}.")
    
    @age.setter
    def age(self, ageValue):
        self.age = ageValue
    
    def say(self):
        self.__say_hi()
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
        


siri = Siri('siri', 5)
siriKo = SiriKo('siriKo', 3)



def commonSay(robot : Robot):
    robot.say()
    
commonSay(siri)
commonSay(siriKo)


robot = Robot('irobot', 100)


bixBy = Bixby("zbix", 7)
#Bixby 클래스의 경우 부모클래스의 메서드 오버라이딩을 하지 않았으므로 부모 클래스 메서드를 호출
bixBy.say()