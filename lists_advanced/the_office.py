def check_happiness(lst: list, fact):

    multiplied_happiness = [x * fact for x in lst]

    average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)

    # count_happy = 0

    # for element in multiplied_happiness:
    #
    #     if element >= average_happiness:
    #         count_happy += 1

    count_happy = sum(x >= average_happiness for x in multiplied_happiness)

    is_happy = False

    if count_happy >= len(multiplied_happiness) / 2:
        is_happy = True

    result = ''

    if is_happy:
        print(f'Score: {count_happy}/{len(multiplied_happiness)}. Employees are happy!')
    else:
        print(f'Score: {count_happy}/{len(multiplied_happiness)}. Employees are not happy!')


initial_list = input().split()

initial_list = list(map(int, initial_list))

factor = int(input())

check_happiness(initial_list, factor)
