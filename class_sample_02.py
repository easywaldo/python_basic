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