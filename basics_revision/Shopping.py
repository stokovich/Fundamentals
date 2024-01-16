budget = int(input())
total = 0

while True:
    line = input()
    if line == 'End':
        break

    price = int(line)

    if total + price > budget:
        print('You went in overdraft!')
        total += price
        break

    total += price

if total <= budget:
    print('You bought everything needed.')