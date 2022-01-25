from typing import Dict, List, TypedDict
from typing import Union


dictSampe: Dict[str, str] = {"name": "easywaldo", "habit" :"python"}

class Point(TypedDict):
    x: int
    y: float
    z: str
    
point: Point = {"x": 8, "y": 0.3, "z": "easywaldo"}    



Value = Union[int, bool, List[int]]
X = int
x: X = 100

value: Value = 17

def cal(v: Value) -> Value:
    return v

print(cal(True))
print(cal(100))