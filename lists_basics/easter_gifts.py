initial_string = input()

my_list = initial_string.split(' ')

while True:
    line = input()
    if line == 'No Money':
        break
    curr_list = line.split(' ')

    if 'OutOfStock' in curr_list:
        for i in range(len(my_list)):
            if my_list[i] == curr_list[1]:
                my_list[i] = 'None'
    elif 'Required' in curr_list:
        curr_index = int(curr_list[2])
        if len(my_list) > curr_index >= 0:
            my_list[curr_index] = curr_list[1]
    elif 'JustInCase' in curr_list:
        my_list[-1] = curr_list[1]

for i in range(len(my_list)):
    if my_list[i] == 'None':
        continue
    else:
        print(my_list[i], end=' ')

