def shooting_game(lst: list):
    targets_hit = 0
    while True:
        curr_line = input()

        if curr_line == 'End':
            break

        curr_index = int(curr_line)

        if curr_index > len(lst) - 1:
            continue

        if lst[curr_index] == -1:
            continue

        curr_target = lst[curr_index]

        for i in range(len(lst)):
            if lst[i] == -1:
                continue

            if i == curr_index:
                lst[i] = -1
                targets_hit += 1
                continue

            if lst[i] > curr_target:
                lst[i] -= curr_target
            else:
                lst[i] += curr_target

    return lst, targets_hit


initial_list = list(map(int, input().split()))

final_list, targets = shooting_game(initial_list)

final_list = list(map(str, final_list))

list_as_string = ' '.join(final_list)

print(f'Shot targets: {targets} -> {list_as_string}')
