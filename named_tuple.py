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


Point = namedtuple('Point', 'x, y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)


# named tuple 4 ways definition
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)

print(Point4)


print(Point1, Point2, Point3, Point4)

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)


print(p1)
print(p2)
print(p3)
print(p4)


temp_dict = {'x': 75, 'y': 55}

p5 = Point3(**temp_dict)
print(p5)
print(p5[0] + p5[1])
print(p5.x + p5.y)


# namedtuple method
temp = [33, 55]
p4 = Point1._make(temp)     # 새로운 개체 생성
print(p4)

print(p1._fields, p2._fields, p3._fields)   # 필드네임 확인

print(p1._asdict())     # OrderedDitc 반환
print(p4._asdict())


Classes = namedtuple('Classes', ['rank', 'number'])

numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

students = [Classes(r, n) for r in ranks for n in numbers]
print(len(students))
print(students)

