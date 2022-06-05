def func(dept: str, name: str, *args):
    print('dept: %s ' % dept)
    print('name: %s ' % name)
    print('===== args =====')
    print(args)


def main():
    func('growth hacking team', 'waldo', 'python', 'java', 'c#', 'mysql', 'mongodb', 'springboot', 'jpg', 'django', 'fastapi', 'nestjs', 'typescript', 'php')


if __name__ == '__main__':
    main()
