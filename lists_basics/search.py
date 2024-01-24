n = int(input())
searched_word = input()
my_list = []

for i in range(n):
    line = input()
    my_list.append(line)

print(my_list)

for i in range(len(my_list) - 1, -1, -1):
    if searched_word not in my_list[i]:
        my_list.remove(my_list[i])

print(my_list)
