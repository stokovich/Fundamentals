my_list = input().split(', ')
new_list = []

for element in my_list:
    new_list.append(int(element))

number_of_zeroes = new_list.count(0)

# print(number_of_zeroes)

for i in range(number_of_zeroes):
    new_list.remove(0)
    new_list.append(0)

print(new_list)


