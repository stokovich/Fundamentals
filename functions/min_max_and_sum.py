def sum_of_list(x):
    return sum(x)


def min_in_list(x):
    return min(x)


def max_in_list(x):
    return max(x)


initial_list = [int(x) for x in input().split()]

print(f'The minimum number is {min_in_list(initial_list)}')
print(f'The maximum number is {max_in_list(initial_list)}')
print(f'The sum number is: {sum_of_list(initial_list)}')

