def reverse_strings():
    while True:
        curr_line = input()

        if curr_line == 'end':
            break

        reversed_word = curr_line[::-1]

        print(f'{curr_line} = {reversed_word}')


reverse_strings()
