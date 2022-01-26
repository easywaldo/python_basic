from typing import Generic, Optional, Union, TypeVar

ARM = TypeVar("ARM")
HEAD = TypeVar("HEAD")


class Robot(Generic[ARM, HEAD]):
    def __init__(self, arm: ARM, head: HEAD):
        self.arm = arm
        self.head = head
        
    def decode(self):
        decodedValue: Optional[ARM] = None
        pass
    
    def __str__(self):
        return f"{self.arm} && {self.head}"
        


robot: Robot = Robot[int, int](122432, 343534)
robot2: Robot = Robot[str, str]("2323544", "84539232")
robot3: Robot = Robot[float, str](345483.135, "249308543")

class Siri(Robot[ARM, HEAD]):
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