number_list = [10, 20, 30, 6, 9, 8, 3, 100, 23, 98];
temp_number = 0
temp_index = 0
index = 0

for number in number_list:
    if number > temp_number:
        temp_index = index
        temp_number = number
    index+=1
print(temp_number)
print(temp_index)



