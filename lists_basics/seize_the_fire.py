initial_string = input()
amount_water = int(input())
total_effort = 0
total_fire = 0
my_list = initial_string.split('#')
fires_list = []
i = 0

for i in range(len(my_list)):
    curr_list = my_list[i].split(' = ')
    fire_type = curr_list[0]
    cell_value = int(curr_list[1])
    if amount_water < cell_value:
        continue
    if fire_type == 'High' and 81 <= cell_value <= 125:
        amount_water -= cell_value
        total_effort += 0.25 * cell_value
        total_fire += cell_value
        fires_list.append(cell_value)
    elif fire_type == 'Medium' and 51 <= cell_value <= 80:
        amount_water -= cell_value
        total_effort += 0.25 * cell_value
        total_fire += cell_value
        fires_list.append(cell_value)
    elif fire_type == 'Low' and 1 <= cell_value <= 50:
        amount_water -= cell_value
        total_effort += 0.25 * cell_value
        total_fire += cell_value
        fires_list.append(cell_value)
    else:
        continue

print('Cells:')
for element in fires_list:
    print(f'- {element}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')



