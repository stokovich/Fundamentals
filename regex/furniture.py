import re


def furniture():
    regex = r'(?<=>>)\w+(?=<<)|(?<=<<)\d+\.?\d*(?=!)|(?<=!)\d+'
    bought_furniture = []
    total_cost = 0

    while True:
        curr_line = input()

        if curr_line == 'Purchase':
            break

        matches = re.findall(regex, curr_line)

        if len(matches) == 3:

            bought_furniture.append(matches[0])

            total_cost += float(matches[1]) * int(matches[2])

    print('Bought furniture:')
    for element in bought_furniture:
        print(element)
    print(f'Total money spend: {total_cost:.2f}')


furniture()
