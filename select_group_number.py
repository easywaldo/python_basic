def select_group_name(name_list):
    group_name = set()

    for name in name_list:
        group_name.add(name)

    print(group_name)

def select_same_name_group(name_list):
    length = len(name_list)
    same_name_list = []
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if (name_list[j] == name_list[i]):
                same_name_list.append(name_list[j])
            
    print(same_name_list)    

select_group_name(['jinam', 'tom', 'jenifer', 'jinam', 'papa', 'denis', 'tom'])

select_same_name_group(['jinam', 'tom', 'jenifer', 'jinam', 'papa', 'denis', 'tom'])
