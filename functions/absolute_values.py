def convert_to_abs(x):
    return abs(x)


initial_list = [float(x) for x in input().split()]
new_list = []

for element in initial_list:
    new_list.append(convert_to_abs(element))

print(new_list)


