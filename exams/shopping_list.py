def make_shopping_list(lst: list):
    while True:
        curr_line = input()

        if curr_line == 'Go Shopping!':
            break

        curr_line = curr_line.split()

        if curr_line[0] == 'Urgent':
            new_item = curr_line[1]

            if new_item in lst:
                continue
            else:
                lst.insert(0, new_item)

        elif curr_line[0] == 'Unnecessary':
            new_item = curr_line[1]

            if new_item in lst:
                lst.remove(new_item)
            else:
                continue

        elif curr_line[0] == 'Correct':
            old_item = curr_line[1]
            new_item = curr_line[2]

            if old_item in lst:
                index = lst.index(old_item)
                lst[index] = new_item
            else:
                continue

        elif curr_line[0] == 'Rearrange':
            new_item = curr_line[1]

            if new_item in lst:
                lst.remove(new_item)
                lst.append(new_item)
            else:
                continue

    lst_as_string = ', '.join(lst)

    print(lst_as_string)


initial_list = input().split('!')

make_shopping_list(initial_list)
