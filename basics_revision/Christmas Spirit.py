quantity = int(input())
days = int(input())

totalSpirit = 0
budget = 0

for day in range(1, days+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += quantity * 2
        totalSpirit += 5
    if day % 3 == 0:
        budget += quantity * 5 + quantity * 3
        totalSpirit += 3 + 10
    if day % 5 == 0:
        budget += quantity * 15
        totalSpirit += 17
    if day % 10 == 0:
        totalSpirit -= 20
        budget += 23
    if day % 5 == 0 and day % 3 == 0:
        totalSpirit += 30

if days % 10 == 0:
    totalSpirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {totalSpirit}')
