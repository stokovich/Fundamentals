def check_strings(first_lst,second_lst):
    new_list = []

    for element in first_lst:
        for second_element in second_lst:
            if element in second_element and element not in new_list:
                new_list.append(element)

    return new_list


first_list = input().split(', ')
second_list = input().split(', ')
result = check_strings(first_list,second_list)
print(result)