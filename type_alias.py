from typing import Dict, TypedDict


dictSampe: Dict[str, str] = {"name": "easywaldo", "habit" :"python"}

class Point(TypedDict):
    x: int
    y: float
    z: str
    
point: Point = {"x": 8, "y": 0.3, "z": 10}    
