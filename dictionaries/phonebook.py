def phonebook():
    n = 0
    phonebook_dict = {}
    while True:
        curr_line = input()

        if "-" not in curr_line:
            n = int(curr_line)
            break

        curr_line = curr_line.split('-')

        name = curr_line[0]
        phone = curr_line[1]

        phonebook_dict[name] = phone

    for i in range(n):
        searched_name = input()

        if searched_name in phonebook_dict.keys():
            number = phonebook_dict[searched_name]
            print(f'{searched_name} -> {number}')
        else:
            print(f'Contact {searched_name} does not exist.')


phonebook()