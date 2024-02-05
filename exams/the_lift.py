def lift_fill(people, lst: list):
    for i in range(len(lst)):
        while lst[i] < 4:
            if people == 0:
                break
            lst[i] += 1
            people -= 1
    return people, lst


def print_result(people, lst: list):
    lst_str = list(map(str, lst))
    result = ' '.join(lst_str)
    if lst[-1] == 4 and people > 0:
        print(f'There isn\'t enough space! {people} people in a queue!')
        print(f'{result}')
    elif lst[-1] == 4 and people == 0:
        print(f'{result}')
    elif lst[-1] < 4 and people == 0:
        print(f'The lift has empty spots!')
        print(f'{result}')


num_of_people = int(input())
wagons = list(map(int, input().split()))

num_of_people, wagons = lift_fill(num_of_people, wagons)
print_result(num_of_people, wagons)