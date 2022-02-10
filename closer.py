def outer(x):
    def inner():
        return x * 10
    return inner()

func = outer(10)
print(func)


def greeting(name, age, gender):
    def inner():
        print(f'{name} 님 안녕하세요')
        print(f'나이 {age}')
        print(f'성별 {gender}')
    return inner

closure = greeting('waldo', 42, 'male')
closure()

print(dir(closure))
print(dir(closure.__closure__))
print(dir(closure.__closure__[0]))
print(closure.__closure__[0].cell_contents)
print(closure.__closure__[1].cell_contents)
print(closure.__closure__[2].cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)