def recursive(data):
    if (data < 0):
        print('ended')
    else:
        print(data)
        recursive(data -1)
        print('returned', data)

def push(num, list):
    list.append(num)

list = list()

push(1, list)
push(2, list)
push(100, list)
pop(list)
pop(list)