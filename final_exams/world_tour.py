def world_tour():
    working_string = input()

    while True:
        curr_line = input()

        if curr_line == 'Travel':
            print(f'Ready for world tour! Planned stops: {working_string}')
            break

        items_list = curr_line.split(':')

        action = items_list[0]

        if action == 'Add Stop':
            index = int(items_list[1])
            string = items_list[2]

            if 0 <= index < len(working_string):
                working_string = working_string[:index] + string + working_string[index:]

        elif action == 'Remove Stop':
            start_index = int(items_list[1])
            end_index = int(items_list[2])

            if 0 <= start_index < len(working_string) and 0 <= end_index < len(working_string):
                working_string = working_string[:start_index] + working_string[end_index + 1:]

        elif action == 'Switch':
            old_string = items_list[1]
            new_string = items_list[2]

            working_string = working_string.replace(old_string, new_string)

        print(working_string)


world_tour()


