count_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
count_shield_broken = 0

for curr_fight in range(1, count_lost_fights + 1):
    if curr_fight % 2 == 0:
        expenses += helmet_price
    if curr_fight % 3 == 0:
        expenses += sword_price
    if curr_fight % 2 == 0 and curr_fight % 3 == 0:
        expenses += shield_price
        count_shield_broken += 1
    if count_shield_broken == 2:
        expenses += armor_price
        count_shield_broken = 0

print(f'Gladiator expenses: {expenses:.2f} aureus')