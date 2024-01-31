import sys

initial_list = [int(x) for x in input().split()]

while True:
    line = input()
    if line == 'end':
        break
# exchanging the string
    if 'exchange' in line:
        working_list = line.split()
        index = int(working_list[1])
        if index < 0 or index > len(initial_list) - 1:
            print('Invalid index')
            continue
        first_list = []
        second_list = []

        for i in range(index + 1):
            first_list.append(initial_list[i])
        for i in range(index + 1, len(initial_list)):
            second_list.append(initial_list[i])
        second_list.extend(first_list)
        initial_list = second_list
# Finding max number odd/even
    elif 'max' in line:
        working_list = line.split()
        type_of_number = working_list[1]
        max_number = - sys.maxsize
        max_index = 0
        is_max = False

        if type_of_number == 'odd':
            for index in range(len(initial_list)):
                curr_element = initial_list[index]
                if curr_element % 2 != 0 and curr_element >= max_number:
                    max_number = curr_element
                    max_index = index
                    is_max = True
        elif type_of_number == 'even':
            for index in range(len(initial_list)):
                curr_element = initial_list[index]
                if curr_element % 2 == 0 and curr_element >= max_number:
                    max_number = curr_element
                    max_index = index
                    is_max = True
        if is_max:
            print(max_index)
        else:
            print('No matches')
# Finding min number odd/even
    elif 'min' in line:
        working_list = line.split()
        type_of_number = working_list[1]
        min_number = sys.maxsize
        min_index = 0
        is_min = False

        if type_of_number == 'odd':
            for index in range(len(initial_list)):
                curr_element = initial_list[index]
                if curr_element % 2 != 0 and curr_element <= min_number:
                    min_number = curr_element
                    min_index = index
                    is_min = True
        elif type_of_number == 'even':
            for index in range(len(initial_list)):
                curr_element = initial_list[index]
                if curr_element % 2 == 0 and curr_element <= min_number:
                    min_number = curr_element
                    min_index = index
                    is_min = True
        if is_min:
            print(min_index)
        else:
            print('No matches')

# Finding the first N elements from the list
    elif 'first' in line:
        working_list = line.split()
        type_of_move = working_list[0]
        count = int(working_list[1])
        initial_count = 0
        type_of_number = working_list[2]
        new_list = []

        if count > len(initial_list):
            print('Invalid count')
            continue

        if type_of_number == 'even':
            for element in initial_list:
                if initial_count == count:
                    break
                if element % 2 == 0:
                    new_list.append(element)
                    initial_count += 1
        elif type_of_number == 'odd':
            for element in initial_list:
                if initial_count == count:
                    break
                if element % 2 != 0:
                    new_list.append(element)
                    initial_count += 1
        print(new_list)

# Find the last N elements from the list
    elif 'last' in line:
        working_list = line.split()
        type_of_move = working_list[0]
        count = int(working_list[1])
        initial_count = 0
        type_of_number = working_list[2]
        new_list = []

        if count > len(initial_list):
            print('Invalid count')
            continue

        if type_of_number == 'even':
            for element in initial_list.__reversed__():
                if initial_count == count:
                    break
                if element % 2 == 0:
                    new_list.append(element)
                    initial_count += 1
        elif type_of_number == 'odd':
            for element in initial_list.__reversed__():
                if initial_count == count:
                    break
                if element % 2 != 0:
                    new_list.append(element)
                    initial_count += 1
        new_list.reverse()
        print(new_list)

print(initial_list)




