def round_number(num):
    return round(num, 0)


initial_list = [float(x) for x in input().split()]
rounded_list = []

for element in initial_list:
    rounded_list.append(int(round_number(element)))

print(f'{rounded_list}')