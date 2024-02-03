def chars_in_range(a, b):
    first_char_int = ord(a)
    second_char_int = ord(b)
    working_list = []

    for i in range(first_char_int + 1,second_char_int):
        working_list.append(chr(i))

    final_string = ' '.join(working_list)

    return final_string


first_char = input()
second_char = input()

print(chars_in_range(first_char, second_char))