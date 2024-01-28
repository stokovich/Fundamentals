my_list = input().split()
initial_string = input()
working_string = initial_string
final_string = ''

for element in my_list:
    sum_of_numbers = 0
    curr_char = ''
    for i in range(len(element)):
        number = int(element[i])
        sum_of_numbers += number
    if sum_of_numbers > len(working_string) - 1:
        curr_index = sum_of_numbers % len(working_string)
    else:
        curr_index = sum_of_numbers
    final_string += working_string[curr_index]

    new_string = working_string[:curr_index] + working_string[curr_index + 1:]

    working_string = new_string

print(final_string)



