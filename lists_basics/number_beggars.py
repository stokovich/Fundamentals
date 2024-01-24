my_string = input()
num_of_beggars = int(input())

my_list = my_string.split(", ")

list_for_beggars = []

for beggar in range(num_of_beggars):
    sum_of_beggar = 0
    while beggar < len(my_list):
        sum_of_beggar += int(my_list[beggar])
        beggar += num_of_beggars
    list_for_beggars.append(sum_of_beggar)

print(list_for_beggars)