first_number = int(input())
second_number = int(input())
exchange_variable = 0

print(f'Before:')
print(f'a = {first_number}')
print(f'b = {second_number}')

exchange_variable = first_number
first_number = second_number
second_number = exchange_variable

print(f'After:')
print(f'a = {first_number}')
print(f'b = {second_number}')