from typing import List, Tuple, Dict


int_var : int  = 88
str_var : str = "hello world"
float_var : float  = 88.99
bool_var : bool = True

int_var = "hello world"
list_var : List[int] = [2,3,4,5,6,7,8,9,10,11]
tuple_var : Tuple[int, ...] = (1,2,3)
dic_var : Dict[str, int] = {"bob": 40, "teo": 22}

def type_check(obj, typeErr) -> None:
    if isinstance(obj, typeErr):
        pass
    else:
        raise TypeError(f"TypeError : {typeErr}")

def cal_add(x : int, y : int) -> int:
    ##type_check(x, int)
    ##type_check(y, int)
    return x + y

print(cal_add(1,3))
print(cal_add("hello", "world"))
print(cal_add([1,2,3], [4,5,6]))
print(tuple_var)

