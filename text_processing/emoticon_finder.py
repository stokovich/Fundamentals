def emoticon_finder():
    initial_string = input()
    emoticon = ''

    for i in range(len(initial_string)):
        char = initial_string[i]

        if char == ":":
            emoticon = char + initial_string[i + 1]
            print(emoticon)


emoticon_finder()
