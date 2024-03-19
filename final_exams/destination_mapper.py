import re


def destination_mapper():
    text = input()
    regex = r'(\/|=)([A-Z][A-Za-z]{2,})\1'
    travel_points = 0
    destinations = []

    matches = re.finditer(regex, text)

    for element in matches:
        destinations.append(element.group(2))
        travel_points += len(element.group(2))

    destinations_as_string = ', '.join(destinations)
    print(f'Destinations: {destinations_as_string}')
    print(f'Travel Points: {travel_points}')


destination_mapper()
