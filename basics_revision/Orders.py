n = int(input())
total = 0

is_correct = False

for i in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())

    total_order = 0

    if 0.01 <= price <= 100.00:
        is_correct = True
    else:
        is_correct = False
        continue

    if 1 <= days <= 31:
        is_correct = True
    else:
        is_correct = False
        continue

    if 1 <= capsules <= 2000:
        is_correct = True
    else:
        is_correct = False
        continue

    if is_correct:
        total_order = price * days * capsules
        print(f'The price for the coffee is: ${total_order:.2f}')
        total += total_order

print(f'Total: ${total:.2f}')

