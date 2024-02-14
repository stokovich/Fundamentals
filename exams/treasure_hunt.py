def calculate_treasure():
    initial_loot = input().split('|')

    while True:
        curr_line = input()

        if curr_line == 'Yohoho!':
            break

        curr_line = curr_line.split()

        if curr_line[0] == 'Loot':

            for i in range(1, len(curr_line)):

                if curr_line[i] in initial_loot:
                    continue
                else:
                    initial_loot.insert(0, curr_line[i])

        elif curr_line[0] == 'Drop':
            index = int(curr_line[1])

            if not 0 <= index < len(initial_loot):
                continue
            else:
                initial_loot.append(initial_loot.pop(index))

        elif curr_line[0] == 'Steal':
            count = int(curr_line[1])
            stolen_loot = []

            if count > len(initial_loot):
                count = len(initial_loot)

            start_index = len(initial_loot) - count

            for i in range(start_index, len(initial_loot)):
                stolen_loot.append(initial_loot[i])

            for i in range(len(initial_loot) -1, start_index - 1, -1):
                initial_loot.pop(i)

            stolen_loot_string = ', '.join(stolen_loot)

            print(stolen_loot_string)

    if len(initial_loot) == 0:
        print(f'Failed treasure hunt.')
    else:
        total_length = 0
        average_gain = 0

        for element in initial_loot:
            total_length += len(element)

        average_gain = total_length / len(initial_loot)

        print(f'Average treasure gain: {average_gain:.2f} pirate credits.')


calculate_treasure()

