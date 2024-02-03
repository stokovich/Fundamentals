def sum_numbers(x, y):
    return x + y


def subtract(a, b):
    return a - b


def add_and_subtract(x, y, z):
    return subtract(sum_numbers(x, y), z)

first_num = int(input())
second_num = int(input())
third_num = int(input())

result = add_and_subtract(first_num, second_num, third_num)

print(result)