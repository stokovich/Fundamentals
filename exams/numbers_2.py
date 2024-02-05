def find_max_numbers(lst: list):
    average_sum = sum(lst) / len(lst)
    final_list = []
    lst.sort(reverse=True)

    for element in lst:
        if len(final_list) == 5:
            break
        if element > average_sum:
            final_list.append(element)

    lst_string = [str(x) for x in final_list]

    if len(final_list) == 0:
        return 'No'
    else:
        return ' '.join(lst_string)


initial_list = [int(x) for x in input().split()]

print(find_max_numbers(initial_list))

