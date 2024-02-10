def find_indexes_even_numbers(lst: list):

    even_numbers = []

    for i in range(len(lst)):

        if lst[i] % 2 == 0:
            even_numbers.append(lst.index(lst[i], i))

    return even_numbers


initial_list = input().split(', ')

initial_list = list(map(int, initial_list))

result = find_indexes_even_numbers(initial_list)

print(result)