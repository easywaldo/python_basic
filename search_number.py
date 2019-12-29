def search_number_in_list(searchNumber, list):
    index = 0
    for item in list:
        if item == searchNumber:
            return index
        index +=1
    
    return -1


print(search_number_in_list(100, [1,2,10, 27, 88, 9, 70, 100, 54, 28, 30, 3]))

        
        