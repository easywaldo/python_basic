import abc

class Unit():
    count = 0
    def __init__(self, hp, name, value):
        self.__hp = 100
        self.name = name
        self.value = value
        Unit.count += 1
    @property
    def hp(self):
        return self.__hp
    def minus(self):
        self.__hp -= 1
    @classmethod
    def getCount(cls):
        return cls.count
    

myUnit = Unit(100, "robot", "waldo")
## getter access
print(myUnit.hp)

## name mangling
myUnit._Unit__hp = 10000
print(myUnit.hp)

print(myUnit.count)
myUnit.count += 1

print(myUnit.count)


print(Unit.getCount())
print(Unit.count)