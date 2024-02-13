def heart_delivery(lst: list):
    curr_position = 0

    while True:
        curr_line = input()

        if curr_line == 'Love!':
            break

        curr_line = curr_line.split()
        jump_length = int(curr_line[1])

        if curr_position + jump_length > len(lst) - 1:
            curr_position = 0
        else:
            curr_position += jump_length

        if lst[curr_position] == 0:
            print(f'Place {curr_position} already had Valentine\'s day.')
        else:
            lst[curr_position] -= 2

            if lst[curr_position] == 0:
                print(f'Place {curr_position} has Valentine\'s day.')


    # print(lst)

    print(f'Cupid\'s last position was {curr_position}.')

    if lst.count(0) == len(lst):
        print(f'Mission was successful.')
    else:
        failed_houses = 0

        for element in lst:
            if element > 0:
                failed_houses += 1

        print(f'Cupid has failed {failed_houses} places.')





initial_list = input().split('@')
initial_list = list(map(int, initial_list))

heart_delivery(initial_list)