import re

dates = input()
regex = r"(\d{2})([/.-])([A-Z][a-z]{2})\2(\d{4})"
matches = re.findall(regex, dates)

#print(matches)

for element in matches:
    day = element[0]
    month = element[2]
    year = element[3]

    print(f'Day: {day}, Month: {month}, Year: {year}')
