def print_diff_numbers(lst: list):
    positive_numbers = [str(x) for x in lst if x >= 0]
    negative_numbers = [str(x) for x in lst if x < 0]
    even_numbers = [str(x) for x in lst if x % 2 == 0]
    odd_numbers = [str(x) for x in lst if x % 2 != 0]

    positive_numbers = ', '.join(positive_numbers)
    negative_numbers = ', '.join(negative_numbers)
    even_numbers = ', '.join(even_numbers)
    odd_numbers = ', '.join(odd_numbers)

    print(f'Positive: {positive_numbers}')
    print(f'Negative: {negative_numbers}')
    print(f'Even: {even_numbers}')
    print(f'Odd: {odd_numbers}')


initial_list = input().split(', ')
initial_list = list(map(int, initial_list))
print_diff_numbers(initial_list)