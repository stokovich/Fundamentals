initial_string = input()
numbers_to_remove = int(input())

my_list = initial_string.split(' ')

my_list_sorted = [int(x) for x in my_list]

my_list_sorted.sort()

for i in range(numbers_to_remove):
    element = str(my_list_sorted[i])

    my_list.remove(element)

for j in range(len(my_list)):
    if j == len(my_list) - 1:
        print(my_list[j], end='')
    else:
        print(my_list[j], end=', ')


