import re


def check_information():
    text = input()
    regex = r'(#|\|)([a-zA-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
    total_calories = 0

    matches = re.finditer(regex, text)

    for element in matches:
        total_calories += int(element.group(4))

    days_last = total_calories // 2000

    print(f'You have food to last you for: {days_last} days!')

    matches = re.finditer(regex, text)

    for match in matches:
        print(f'Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}')


check_information()
