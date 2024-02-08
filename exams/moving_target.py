def hit_moving_targets(lst: list):


    while True:
        curr_line = input()

        if curr_line == 'End':
            break

        curr_line = curr_line.split()
        type_movement = curr_line[0]
        index = int(curr_line[1])
        value_radius = int(curr_line[2])

        if type_movement == 'Shoot':

            if not 0 <= index <= len(lst) - 1:
                continue
            else:
                lst[index] -= value_radius

            if lst[index] <= 0:
                lst.pop(index)

        if type_movement == 'Add':

            if 0 <= index <= len(lst) - 1:
                lst.insert(index, value_radius)
            else:
                print('Invalid placement!')

        if type_movement == 'Strike':

            if index - value_radius < 0 or index + value_radius >= len(lst):
                print('Strike missed!')
                continue
            else:
                for i in range(index + value_radius, index - value_radius - 1, -1):
                    lst.pop(i)

    lst = list(map(str, lst))

    lst_as_string = '|'.join(lst)

    return lst_as_string


initial_list = input().split()

initial_list = list(map(int, initial_list))

result = hit_moving_targets(initial_list)

print(result)


