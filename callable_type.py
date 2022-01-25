from typing import Callable


def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))

def foo(func: Callable[[int, int], int]):
    return func(2,3)

def test():
    pass


print(foo(add))