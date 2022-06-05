def func(dept: str, name: str, *args, **kargs):
    print('dept: %s ' % dept)
    print('name: %s ' % name)
    print('===== args =====')
    print(kargs.get('city'))
    print(kargs.get('dept'))
    print(kargs.get('age'))
    print(kargs.get('language'))


def main():
    me = {
        'age': 42, 
        'city': 'seoul', 
        'language': ['python', 'java', 'c#']
    }
    func('growth hacking team', 'waldo', None, **me)


if __name__ == '__main__':
    main()
