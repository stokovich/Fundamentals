def manage_inventory(lst: list):
    while True:

        curr_line = input()

        if curr_line == 'Craft!':
            break

        curr_line = curr_line.split(' - ')
        type_movement = curr_line[0]

        if type_movement == 'Collect':
            new_item = curr_line[1]

            if new_item in lst:
                continue
            else:
                lst.append(new_item)

        elif type_movement == 'Drop':
            new_item = curr_line[1]

            if new_item in lst:
                lst.remove(new_item)

        elif type_movement == 'Combine Items':
            items_pack = curr_line[1]
            items_pack = items_pack.split(':')
            old_item = items_pack[0]
            new_item = items_pack[1]

            if old_item in lst:
                old_index = lst.index(old_item)
                lst.insert(old_index + 1, new_item)
            else:
                continue

        elif type_movement == 'Renew':
            new_item = curr_line[1]

            if new_item in lst:
                new_index = lst.index(new_item)
                lst.append(lst.pop(new_index))

    lst_as_string = ', '.join(lst)

    print(lst_as_string)


initial_list = input().split(', ')

manage_inventory(initial_list)

