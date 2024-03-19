def text_filter():
    banned_words = input().split(', ')
    initial_string = input()

    for element in banned_words:
        initial_string = initial_string.replace(element, '*' * len(element))

    return initial_string


print(text_filter())
