import timeit


class Point3D:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)


def main():
    start = timeit.default_timer()

    p1 = Point3D(1, 1, 1)
    p2 = Point3D(21, 21, 41)
    print(p1)
    print(p2)
    # p1.w = 30    # error

    for i in range(10000):
        for i in range(3000):
            p1.x += 1
            p1.y += 1
            p1.z += 1

    print(p1)
    stop = timeit.default_timer()
    print(stop - start)

    # slots >> 6.794247002
    # none slosts >> 9.473876564


if __name__ == '__main__':
    main()
