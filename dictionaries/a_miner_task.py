def find_goods():
    stocks = {}

    while True:
        curr_line = input()

        if curr_line == 'stop':
            break

        item = curr_line
        quantity = int(input())

        if item not in stocks.keys():
            stocks[item] = 0

        stocks[item] += quantity

    for item, quantity in stocks.items():
        print(f"{item} -> {quantity}")


find_goods()