def manage_phones():
    phone_list = input().split(', ')

    while True:
        curr_line = input()

        if curr_line == 'End':
            break

        curr_line = curr_line.split(' - ')
        command = curr_line[0]

        if command == 'Add':
            new_phone = curr_line[1]

            if new_phone in phone_list:
                continue
            else:
                phone_list.append(new_phone)

        elif command == 'Remove':
            phone = curr_line[1]

            if phone in phone_list:
                phone_list.remove(phone)
            else:
                continue

        elif command == 'Bonus phone':
            curr_list = curr_line[1].split(':')
            old_phone = curr_list[0]
            new_phone = curr_list[1]

            if old_phone in phone_list:
                index = phone_list.index(old_phone)
                phone_list.insert(index + 1, new_phone)
            else:
                continue

        elif command == 'Last':
            phone = curr_line[1]

            if phone in phone_list:
                index = phone_list.index(phone)
                phone_list.append(phone_list.pop(index))
            else:
                continue

    phone_list_as_string = ', '.join(phone_list)

    print(phone_list_as_string)


manage_phones()
