def find_even_sum(number):
    num_to_string = str(number)
    sum_even = 0
    for num in num_to_string:
        curr_num = int(num)
        if curr_num % 2 == 0:
            sum_even += curr_num
    return sum_even


def find_odd_sum(number):
    num_to_string = str(number)
    sum_odd = 0
    for num in num_to_string:
        curr_num = int(num)
        if curr_num % 2 != 0:
            sum_odd += curr_num
    return sum_odd


input_number = int(input())

final_even_sum = find_even_sum(input_number)
final_odd_sum = find_odd_sum(input_number)

print(f'Odd sum = {final_odd_sum}, Even sum = {final_even_sum}')
