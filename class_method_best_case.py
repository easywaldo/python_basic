class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def show(self):
        print('{0}, {1}, {2}'.format(self.year, self.month, self.day))

    @classmethod
    def next_day(cls, today):
        return cls(today.year, today.month, today.day + 1)


class KDate(Date):
    def show(self):
        print('KOR: {0}, {1}, {2}'.format(self.year, self.month, self.day))


class JDate(Date):
    def show(self):
        print('JPN: {0}, {1}, {2}'.format(self.year, self.month, self.day))


def main():
    kd1 = KDate(2025, 4, 12)
    kd1.show()
    kd2 = KDate.next_day(kd1)
    kd2.show()

    jd1 = JDate(2027, 5, 19)
    jd1.show()
    jd2 = JDate.next_day(jd1)
    jd2.show()


main()
