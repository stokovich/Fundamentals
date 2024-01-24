factor_num = int(input())
count = int(input())
my_list = []

for num in range(1, count + 1):
    element = factor_num * num
    my_list.append(element)

print(my_list)
