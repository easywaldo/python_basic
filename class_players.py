class Players:

    _ownGas = 0
    _ownMineral = 0
    _ownUnitList = []
    
    def __init__(self, _ownMineral, _ownGas, _ownUnitList):
        Players._ownGas = _ownGas
        Players._ownMineral = _ownMineral
        Players._ownUnitList = _ownUnitList
    
    @classmethod
    def showUnitList(cls):
        for unit in cls._ownUnitList:
            print(f'{unit.nickName, unit.mineral, unit.gas, unit.hp, unit.defense, unit.ofense}')
        
    @classmethod
    def produce(self, nickName, mineral, gas, hp, defense, ofense):
        
        print("test")
        print(Players._ownGas)
        print(Players._ownMineral)
        
        print(mineral)
        print(gas)
        
        if Players._ownGas < gas:
            print(f'가스가 {gas - Players._ownGas} 만큼 부족합니다.')
        if Players._ownMineral < mineral:
            print(f'미네랄이 {mineral - Players._ownMineral} 만큼 부족합니다.')
 
        unit: Unit = Unit(nickName, mineral, gas, hp, defense, ofense)
        
        print(unit)
        Players._ownUnitList.append(unit)
    
class Unit:
    def __init__(self, nickName, mineral, gas, hp, defense, ofense):
        self.nickName = nickName
        self.mineral = mineral
        self.gas = gas
        self.hp = hp
        self.defense = defense
        self.ofense = ofense
        
p1: Players = Players(1000, 1000, [])
p1.produce('질럿', 100, 100, 50, 9, 2)    
p1.produce('드라군', 125, 80, 200, 12, 5)
p1.produce('템플러', 50, 200, 100, 4, 20)

p1.showUnitList()