initial_list = input().split()
integer_list = []
left_racer_time = 0
right_racer_time = 0

for element in initial_list:
    integer_list.append(int(element))

half_list = len(integer_list) // 2

for i in range(half_list):
    element = integer_list[i]
    if element == 0:
        left_racer_time -= left_racer_time * 0.20
    left_racer_time += element

for i in range(-1, -half_list - 1, -1):
    element = integer_list[i]
    if element == 0:
        right_racer_time -= right_racer_time * 0.20
    right_racer_time += element

if left_racer_time < right_racer_time:
    print(f'The winner is left with total time: {left_racer_time:.1f}')
else:
    print(f'The winner is right with total time: {right_racer_time:.1f}')
