##print(type([1,2,3,4,5,6].__iter__()))

from typing import Iterator


iter_obj = [1,2,3,4,5,6].__iter__()
print(dir(iter_obj))

    
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())

for i in iter_obj:
    print(i)


class Season():
    def __init__(self):
        self.seanson_list = ['spring', 'summer', 'autumn', 'winter']
        self.idx = 0
        self.max_num = 4
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < self.max_num:
            curr_idx = self.idx
            self.idx += 1
            return self.seanson_list[curr_idx]
        else:
            raise StopIteration
        
my_seanson:Season = Season()

print(my_seanson.__next__())
print(my_seanson.__next__())
print(my_seanson.__next__())
print(my_seanson.__next__())
print('1 loop')

for s in my_seanson:
    print(s)

print('2 loop')
for s in my_seanson:
    print(s)