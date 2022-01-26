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



print(robot)
print(robot2)
print(robot3)