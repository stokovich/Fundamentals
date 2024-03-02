def make_statistics():
    products = {}

    while True:
        curr_line = input().split(': ')

        if curr_line[0] == 'statistics':
            break

        product = curr_line[0]
        quantity = int(curr_line[1])

        if product in products.keys():
            products[product] += quantity
        else:
            products[product] = quantity

    print(f'Products in stock:')
    for key, value in products.items():
        print(f'- {key}: {value}')

    count_all_products = len(products)
    sum_all_products = sum(value for value in products.values())

    print(f'Total Products: {count_all_products}')
    print(f'Total Quantity: {sum_all_products}')


make_statistics()