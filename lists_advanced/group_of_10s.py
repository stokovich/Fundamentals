def sort_groups(lst: list):
    filtered_numbers = []
    max_number = 10

    while True:
        if len(lst) == 0:
            break

        filtered_numbers = list(filter(lambda x: x <= max_number, lst))

        for element in filtered_numbers:
            lst.remove(element)

        print(f'Group of {max_number}\'s: {filtered_numbers}')

        max_number += 10


initial_list = input().split(', ')

initial_list = list(map(int, initial_list))

sort_groups(initial_list)

