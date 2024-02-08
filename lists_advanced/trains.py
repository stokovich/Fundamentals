def people_calculations(lst: list):

    while True:

        curr_line = input().split()
        type_movement = curr_line[0]

        if type_movement == 'End':
            break

        if type_movement == 'add':
            lst[-1] += int(curr_line[1])

        elif type_movement == 'insert':
            lst[int(curr_line[1])] += int(curr_line[2])

        elif type_movement == 'leave':
            lst[int(curr_line[1])] -= int(curr_line[2])

    return lst


wagon_length = int(input())

wagon_train = [0] * wagon_length

result = people_calculations(wagon_train)

print(result)
