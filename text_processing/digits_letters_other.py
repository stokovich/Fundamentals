def divide_chars():
    initial_string = input()

    numbers = ''
    letters = ''
    others = ''

    for char in initial_string:
        if char.isnumeric():
            numbers += char
        elif char.isalpha():
            letters += char
        elif not char.isalnum():
            others += char

    print(numbers)
    print(letters)
    print(others)


divide_chars()
