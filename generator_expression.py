import sys

double_generator = [i * 2 for i in range(1,10)]
double_generator_ex = (i * 2 for i in range(1,10))
print(double_generator)
print(double_generator_ex)

# print(double_generator_ex.__next__())
# print(double_generator_ex.__next__())
# print(double_generator_ex.__next__())
# print(double_generator_ex.__next__())
# print(double_generator_ex.__next__())
# print(double_generator_ex.__next__())
# print(double_generator_ex.__next__())
# print(double_generator_ex.__next__())
# print(double_generator_ex.__next__())

for i in double_generator_ex:
    print(i)

list_data = [1 * 3 for i in range(1, 10000 + 1)]
list_generator = (1 * 3 for i in range(1, 10000 + 1))

## 리스트는 저장에 필요한 메모리를 모두 사용
print(sys.getsizeof(list_data))
## 제너레이터는 나중에 필요할 때 값을 만들어서 사용
print(sys.getsizeof(list_generator))
    
