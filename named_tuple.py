from collections import namedtuple

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print(f'This duck has a {self.bill.description}, bill and a {self.tail.length}')

duck = namedtuple("Duck", 'bill tail')
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)

print(f'{duck2.bill} {duck2.tail}')