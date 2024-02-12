def analyze_data(lst: list):
    while True:
        curr_line = input()

        if curr_line == '3:1':
            break

        curr_line = curr_line.split()

        type_movement = curr_line[0]

        if type_movement == 'merge':
            start_index = int(curr_line[1])
            end_index = int(curr_line[2])

            # if not 0 <= start_index < len(lst) and not 0 <= end_index < len(lst):
            #     continue
            # elif not 0 <= start_index < len(lst):
            #     start_index = 0
            # elif not 0 <= end_index < len(lst):
            #     end_index = len(lst) - 1

            if start_index < 0 and end_index >= len(lst):
                start_index = 0
                end_index = len(lst) - 1
            if start_index > len(lst) - 1:
                continue
            if end_index < 0:
                continue
            if start_index < 0 and 0 <= end_index < len(lst):
                start_index = 0
            if end_index > len(lst) - 1 and 0 <= start_index < len(lst):
                end_index = len(lst) - 1

            result = ''

            for i in range(start_index, end_index + 1):
                result += lst[i]

            for i in range(end_index, start_index - 1, -1):
                lst.pop(i)

            lst.insert(start_index, result)

        elif type_movement == 'divide':
            index = int(curr_line[1])
            partitions = int(curr_line[2])
            string = lst[index]

            substring_length = len(string) // partitions

            result = [string[i:i + substring_length] for i in range(0, len(string), substring_length)]

            if len(string) % partitions != 0:
                result[-2] = result[-2] + result[-1]
                result.pop()

            lst.pop(index)

            for i in range(len(result)):
                lst.insert(index + i, result[i])

    lst_as_string = ' '.join(lst)

    print(lst_as_string)


initial_list = input().split()

analyze_data(initial_list)


