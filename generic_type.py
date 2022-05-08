from typing import Generic, Optional, Union, TypeVar

A = TypeVar("A", int, float, str)
H = TypeVar("H", int, float, str)
T = TypeVar("T", int, float, str)


class Robot(Generic[A, H]):
    def __init__(self, arm: A, head: H):
        self.arm = arm
        self.head = head
        
    def decode(self):
        decodedValue: Optional[A] = None
        pass
    
    def __str__(self):
        return f"{self.arm} && {self.head}"
        


robot: Robot = Robot[int, int](122432, 343534)
robot2: Robot = Robot[str, str]("2323544", "84539232")
robot3: Robot = Robot[float, str](345483.135, "249308543")

class Siri(Robot[A, H]):
    pass
        

siri1 = Siri[int, int](342323, 9238235)
siri2 = Siri[str, int]("9999", 245324)
siri3 = Siri[float, str](230845.4523, "12948")


print(robot)
print(robot2)
print(robot3)

print(siri1)
print(siri2)
print(siri3)



### function
def test(x: T) -> T:
    print(x)
    print(type(x))
    return x

test(10000)


print(Siri.mro())