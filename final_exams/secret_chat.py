def secret_chat():
    working_string = input()

    while True:
        curr_line = input()

        if curr_line == 'Reveal':
            print(f'You have a new text message: {working_string}')
            break

        curr_line = curr_line.split(':|:')

        action = curr_line[0]

        if action == 'InsertSpace':
            index = int(curr_line[1])

            working_string = working_string[:index] + ' ' + working_string[index:]

            print(working_string)

        if action == 'Reverse':
            substring = curr_line[1]
            reversed_substring = substring[::-1]

            if substring in working_string:
                start_index = working_string.find(substring)
                end_index = start_index + len(substring)

                working_string = working_string[:start_index] + working_string[end_index:] + reversed_substring
                print(working_string)
            else:
                print('error')

        if action == 'ChangeAll':
            old_substring = curr_line[1]
            new_substring = curr_line[2]

            working_string = working_string.replace(old_substring, new_substring)
            print(working_string)


secret_chat()
