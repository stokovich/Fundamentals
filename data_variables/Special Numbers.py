n = int(input())

for number in range(1, n + 1):
    curr_number = number
    total = 0

    while curr_number > 0:
        total += curr_number % 10
        curr_number = int(curr_number / 10)

    is_special = False

    if total == 5 or total == 7 or total == 11:
        is_special = True
    else:
        is_special = False

    print(f'{number} -> {is_special}')