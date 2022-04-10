# sorted vs sort
# sorted 는 정렬 후 새로운 개체 반환


import array


f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted', sorted(f_list))
print(f_list)

print('sorted', sorted(f_list, reverse=True))
print('sorted', sorted(f_list, key=len))
print('sorted', sorted(f_list, key=lambda x: x[-1]))
print('sorted', sorted(f_list, key=lambda x: x[-1], reverse=True))


print(f_list)

print('sort', f_list.sort(), f_list)
print(f_list)
print('sort', f_list.sort(reverse=True, key=len), f_list)
print(f_list)
print('sort', f_list.sort(reverse=True, key=lambda x: x[-1]), f_list)
print(f_list)

# list vs Array 적합한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열이 적합(리스트와 거의 호환)


num_arr = array.array('d', [1,2,3,4,5,6,7,8,9,10])
print(num_arr)
num_arr.append(11)
print(num_arr)
print(num_arr.itemsize)
num_arr.extend([100, 200, 300])
print(num_arr)
