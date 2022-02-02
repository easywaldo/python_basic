import random


class Monster:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        print('move...')
        
class Shark(Monster):
    def move(self):
        print('swimming')

class Wolf(Monster):
    pass

monster = Monster('alpha')
sharky = Shark('zoss')
wolverin = Wolf('wolverin')

monster.move()
sharky.move()
wolverin.move()

class Dragon(Monster):
    def __init__(self, name, skill):
        super().__init__(name)
        self.skill = skill
    def move(self):
        print(f'{self.name} flying..')
    def doSkill(self):
        print(f'{self.skill[random.randint(0, 3)]} doing..')
        
dragon:Dragon = Dragon('azushara', ('fire', 'lighting', 'crash', 'blizzard'))
dragon.move()
dragon.doSkill()


def doMove(monster:Monster):
    print('funcion do move..')
    monster.move()
    
doMove(monster)
doMove(sharky)
doMove(wolverin)
