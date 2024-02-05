def memory_game(lst: list):
    number_of_moves = 0
    while True:
        curr_move_initial = input()

        if len(lst) == 0:
            print(f'You have won in {number_of_moves} turns!')
            break

        if curr_move_initial == 'end':
            break

        curr_move = list(map(int, curr_move_initial.split()))

        first_index = curr_move[0]
        second_index = curr_move[1]
        number_of_moves += 1

        if not 0 <= first_index <= len(lst) - 1 or not 0 <= second_index <= len(lst) - 1\
                or first_index == second_index:
            middle_index = int(len(lst) / 2)
            element_to_append = '-' + str(number_of_moves) + 'a'
            lst.insert(middle_index, element_to_append)
            lst.insert(middle_index, element_to_append)
            print(f'Invalid input! Adding additional elements to the board')
            continue

        first_item = lst[first_index]
        second_item = lst[second_index]

        if first_item == second_item:
            lst.remove(first_item)
            lst.remove(first_item)
            print(f'Congrats! You have found matching elements - {first_item}!')
        else:
            print(f'Try again!')

    if len(lst) > 0:
        result = ' '.join(lst)
        print(f'Sorry you lose :(')
        print(f'{result}')


sequence = input().split()

memory_game(sequence)
