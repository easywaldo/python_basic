from typing import Union

x: Union[int, str] = 3
x = "hello"


def foo(x: Union[int, str]) -> None:
    print(x)
    
print(x)