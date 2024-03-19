def plant_discovery():
    n = int(input())
    information_for_plants = dict()

    for i in range(n):
        curr_line=input().split('<->')
        information_for_plants[curr_line[0]] = [int(curr_line[1]), []]

    while True:
        curr_line = input()

        if curr_line == 'Exhibition':
            break

        curr_line = curr_line.split(': ')
        action = curr_line[0]

        if action == 'Rate':
            items = curr_line[1].split(' - ')
            plant = items[0]
            rating = float(items[1])

            if plant in information_for_plants.keys():
                information_for_plants[plant][1].append(rating)
            else:
                print(f'error')

        if action == 'Update':
            items = curr_line[1].split(' - ')
            plant = items[0]
            new_rarity = int(items[1])

            if plant in information_for_plants.keys():
                information_for_plants[plant][0] = new_rarity
            else:
                print(f'error')

        if action == 'Reset':
            plant = curr_line[1]

            if plant in information_for_plants.keys():
                information_for_plants[plant][1].clear()
            else:
                print(f'error')

    print(f'Plants for the exhibition:')

    for plant,values in information_for_plants.items():
        if len(values[1]) != 0:
            average_rating = sum(values[1]) / len(values[1])
        else:
            average_rating = 0

        print(f'- {plant}; Rarity: {values[0]}; Rating: {average_rating:.2f}')


plant_discovery()
