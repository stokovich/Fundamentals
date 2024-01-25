train_ticket_cost = 150
initial_list = input().split('|')
budget = float(input())
initial_budget = budget

max_price_clothes = 50
max_price_shoes = 35
max_price_accessories = 20.50

bought_items = []
sold_items = []

for element in initial_list:
    current_list = element.split('->')
    item_type = current_list[0]
    item_price = float(current_list[1])
    item_price_valid = False

    if item_type == 'Clothes' and item_price <= 50.00:
        item_price_valid = True
    elif item_type == 'Shoes' and item_price <= 35.00:
        item_price_valid = True
    elif item_type == 'Accessories' and item_price <= 20.50:
        item_price_valid = True

    if item_price_valid and budget >= item_price:
        bought_items.append(item_price)
        budget -= item_price

for element in bought_items:
    sold_items.append(element * 1.40)

total_sold = sum(sold_items)
total_bought = sum(bought_items)

profit = total_sold - total_bought

for i in range(len(sold_items)):
    if i < len(sold_items) - 1:
        print(f'{sold_items[i]:.2f}', end=' ')
    else:
        print(f'{sold_items[i]:.2f}')

print(f'Profit: {profit:.2f}')

if profit + initial_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')

