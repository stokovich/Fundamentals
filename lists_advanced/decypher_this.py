import re

def decipher_func(lst: list):
    final_list = []

    for element in lst:
        parts = re.split(r"(\d+)", element)
        first_part = chr(int(parts[1]))

        second_part = [x for x in parts[2]]

        second_part[0], second_part[-1] = second_part[-1], second_part[0]

        result = first_part + ''.join(second_part)

        final_list.append(result)

    final_list_as_string = ' '.join(final_list)

    print(final_list_as_string)


initial_list = input().split()

decipher_func(initial_list)
