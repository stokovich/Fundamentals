def change_version(lst: list):
    if lst[2] < 9:
        lst[2] += 1
    else:
        lst[2] = 0
        if lst[1] < 9:
            lst[1] += 1
        else:
            lst[1] = 0
            lst[0] += 1

    lst = list(map(str, lst))
    lst_as_string = '.'.join(lst)
    return lst_as_string


initial_version = input().split('.')
initial_version = list(map(int, initial_version))
result = change_version(initial_version)
print(result)