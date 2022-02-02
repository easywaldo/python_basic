version = 2.0

def printAuthor():
    print('start coding')

class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    def getPayInfo(self):
        return f'{self.id} {self.price} {self.time}'
    
