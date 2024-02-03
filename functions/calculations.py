def calculations(operator_type, first_num, second_num):
    if operator_type == 'multiply':
        return first_num * second_num
    elif operator_type == 'divide':
        if second_num == 0:
            return None
        else:
            return first_num / second_num
    elif operator_type == 'add':
        return first_num + second_num
    elif operator_type == 'subtract':
        return first_num - second_num


operator_input = input()
first_number = int(input())
second_number = int(input())

result = calculations(operator_input, first_number, second_number)

print(f'{result:.0f}')