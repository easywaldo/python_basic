print(sorted("This is a test string from Andrew".split(), key=str.lower))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age))



from operator import itemgetter, attrgetter

print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('grade')))


print(sorted(student_tuples, key=itemgetter(1,2)))
print(sorted(student_objects, key=attrgetter('name', 'grade')))


print(sorted(student_tuples, key=itemgetter(2), reverse=True))
print(sorted(student_objects, key=attrgetter('name', 'grade'), reverse=False))


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        print(f'keys is {key}')
        print(f'reverse is {reverse}')
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs

print(multisort(list(student_objects), (('grade', True), ('age', False))))