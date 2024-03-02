def search_stock():
    initial_list = input().split()
    searched_products = input().split()
    products = {}

    for i in range(0, len(initial_list), 2):
        key = initial_list[i]
        value = initial_list[i + 1]

        products[key] = value

    for element in searched_products:
        if element in products.keys():
            print(f'We have {products[element]} of {element} left')
        else:
            print(f'Sorry, we don\'t have {element}')


search_stock()
