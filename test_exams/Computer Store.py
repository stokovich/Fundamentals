total_price = 0
taxes = 0
total_price_without_taxes = 0
is_special = False

while True:
    line = input()

    if line == 'special' or line == 'regular':
        if line == 'special':
            is_special = True
        break

    price = float(line)

    if price < 0:
        print('Invalid price!')
    else:
        total_price += price

total_price_without_taxes = total_price

taxes = total_price * 0.20

total_price += taxes

if is_special:
    total_price -= total_price * 0.10

if total_price == 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')

