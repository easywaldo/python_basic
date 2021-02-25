listData = list()

def enqueue(num):
    listData.append(num)
def dequeue():
    data = listData[0]
    del listData[0]
    return data

for n in range(10):
    enqueue(n)


listData

dequeue()