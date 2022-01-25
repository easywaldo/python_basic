from typing import Optional, Union


x: Union[str, None] = "easywaldo"
x = None

y: Optional[str] = "easywaldo"


def foo(name: Optional[str]) -> Optional[str]:
    if name == "easywaldo":
        return name
    else:
        return "name is empty"
    
print(foo(x))
print(foo(y))