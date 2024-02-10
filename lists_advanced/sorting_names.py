def sort_names(lst: list):
    sorted_list = sorted(lst, key=lambda x: (-len(x), x))
    return sorted_list


initial_list = input().split(', ')

result = sort_names(initial_list)

print(result)

