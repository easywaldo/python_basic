class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
wos = WithoutSlotClass('wos-instance', 100)

print(wos.__dict__)

wos.__dict__["hello"] = "world"

print(wos.__dict__)


class WithSlotClass:
    __slots__ =["name", "age"]
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
ws = WithSlotClass("ws_instance", 99)
print(ws.__slots__)


import timeit

#* 메모리 사용량 비교

def repeat(obj):
    def inner():
        obj.name = "hello"
        obj.age = 1000
        del obj.name
        del obj.age
    return inner
        
use_slot_time = timeit.repeat(repeat(ws), number = 9999)
no_slot_time = timeit.repeat(repeat(wos), number = 9999)

print("use slot time: ", min(use_slot_time))
print("no slot time: ", min(no_slot_time))