def find_min_value(number_list):
    n = len(number_list)
    min_idx = 0

    for i in range(0, n -1):
        if number_list[i] < number_list[min_idx]:
            min_idx = i
        return min_idx
        

def select_sort(number_list):
    result = []
    while number_list:
        minIdx = find_min_value(number_list)
        value = number_list.pop(minIdx)
        result.append(value)
    return result

number_list = [2, 4, 10, 9, 5, 11]
print(find_min_value(number_list))
