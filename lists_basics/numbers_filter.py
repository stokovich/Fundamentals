n = int(input())
my_list = []

for i in range(n):
    number = int(input())
    my_list.append(number)

my_command = input()

if my_command == 'even':
    for j in range(len(my_list) - 1, -1, -1):
        element = my_list[j]

        # if element % 2 != 0 and element != 0:
        if element % 2 != 0:
            my_list.remove(element)

if my_command == 'odd':
    for j in range(len(my_list) - 1, -1, -1):
        element = my_list[j]

        # if element % 2 == 0 and element == 0:
        if element % 2 == 0:
            my_list.remove(element)

if my_command == 'negative':
    for j in range(len(my_list) - 1, -1, -1):
        element = my_list[j]

        if element >= 0:
            my_list.remove(element)

if my_command == 'positive':
    for j in range(len(my_list) - 1, -1, -1):
        element = my_list[j]

        if element < 0:
            my_list.remove(element)

print(my_list)