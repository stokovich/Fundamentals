def calculate_price(type_stock, quantity):
    if type_stock == 'coffee':
        return quantity * 1.50
    elif type_stock == 'coke':
        return quantity * 1.40
    elif type_stock == 'water':
        return quantity * 1.00
    elif type_stock == 'snacks':
        return quantity * 2.00


stock = input()
number = int(input())
print(f'{calculate_price(stock, number):.2f}')