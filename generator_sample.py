def seanson_generator(*args):
    for arg in args:
        yield arg
        
g = seanson_generator('spring', 'summer', 'atumn', 'winter')
print(g)
print("dir displayed ############")
print(dir(g))

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

def func():
    print('첫번째 작업중')
    yield 1
    
    print('두번째 작업중')
    yield 2
    
ge = func()
data = ge.__next__()
print(data)

data = ge.__next__()
print(data)