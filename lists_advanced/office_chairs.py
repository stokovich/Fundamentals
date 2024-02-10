def check_free_chairs():
    n = int(input())
    all_ok = True
    free_chairs = 0
    for i in range(1, n + 1):
        curr_line = input().split()
        number_chairs = len(curr_line[0])
        people = int(curr_line[1])

        if number_chairs < people:
            print(f'{people - number_chairs} more chairs needed in room {i}')
            all_ok = False
        else:
            free_chairs += number_chairs - people

    if all_ok:
        print(f'Game On, {free_chairs} free chairs left')


check_free_chairs()


