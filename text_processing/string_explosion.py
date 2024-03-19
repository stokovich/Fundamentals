def string_explosion():
    initial_string = input()
    power = 0
    new_string = ''

    for i in range(len(initial_string)):
        char = initial_string[i]

        if power > 0 and char != '>':
            power -= 1
            continue

        if char == '>':
            power += int(initial_string[i + 1])

        new_string += char

    print(new_string)


string_explosion()



