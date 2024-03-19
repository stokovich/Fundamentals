import re


def capture_numbers():
    regex = r'\d+'
    final_list = []

    while True:
        curr_line = input()

        if curr_line == '':
            break

#        print(curr_line)

        matches = re.findall(regex, curr_line)

        for element in matches:

            if element != '':
                final_list.append(element)

#    print(final_list)

    print(' '.join(final_list))


capture_numbers()
