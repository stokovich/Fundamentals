def array_modifier(lst: list):
    while True:
        curr_list = input()

        if curr_list == 'end':
            break

        curr_list = curr_list.split()
        type_move = curr_list[0]

        if type_move == 'swap':
            first_index = int(curr_list[1])
            second_index = int(curr_list[2])
            lst[first_index], lst[second_index] = lst[second_index], lst[first_index]

        elif type_move == 'multiply':
            first_index = int(curr_list[1])
            second_index = int(curr_list[2])

            lst[first_index] = lst[first_index] * lst[second_index]

        elif type_move == 'decrease':
            lst = list(map(lambda x: x - 1, lst))

    lst = [str(x) for x in lst]

    return ', '.join(lst)


initial_list = list(map(int, input().split()))

print(array_modifier(initial_list))
