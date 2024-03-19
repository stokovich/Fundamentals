def orders():
    dict_items = {}

    while True:
        curr_line = input()

        if curr_line == 'buy':
            break

        curr_line = curr_line.split()

        item = curr_line[0]
        quantity = int(curr_line[2])
        price = float(curr_line[1])

        if item not in dict_items.keys():
            dict_items[item] = [0, 0.00]

        dict_items[item][0] += quantity
        dict_items[item][1] = price

    for item, values in dict_items.items():
        total_price = values[0] * values[1]

        print(f'{item} -> {total_price:.2f}')


orders()