def calculate_factorial(n):
    if n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


def calculate_final_result(a, b):
    first_fact = calculate_factorial(a)
    second_fact = calculate_factorial(b)
    result = first_fact / second_fact
    return result


first_num = int(input())
second_num = int(input())

print(f'{calculate_final_result(first_num, second_num):.2f}')

