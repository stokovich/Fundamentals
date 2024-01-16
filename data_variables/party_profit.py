from math import floor

group_size = int(input())
days = int(input())
coins_earned = 0

for curr_day in range(1, days + 1):
    if curr_day % 10 == 0:
        group_size -= 2
    if curr_day % 15 == 0:
        group_size += 5

    coins_earned += 50
    coins_earned -= 2 * group_size

    if curr_day % 3 == 0:
        coins_earned -= 3 * group_size
    if curr_day % 5 == 0:
        coins_earned += 20 * group_size

    if curr_day % 3 == 0 and curr_day % 5 == 0:
        coins_earned -= 2 * group_size

coins_per_companion = floor(coins_earned / group_size)

print(f'{group_size} companions received {coins_per_companion} coins each.')