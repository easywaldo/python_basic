class Father:
    def run(self):
        print('so fast!!')


class Son(Father):
    def jump(self):
        print('so high')


def main():
    s = Son()
    s.run()
    s.jump()

main()