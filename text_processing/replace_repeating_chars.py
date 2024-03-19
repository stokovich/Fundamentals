def replace_repeating():
    initial_string = input()
    new_string = ''

    for i in range(len(initial_string)):
        if i == 0:
            new_string += initial_string[i]
        elif initial_string[i] == initial_string[i - 1]:
            continue
        else:
            new_string += initial_string[i]

    print(new_string)


replace_repeating()

