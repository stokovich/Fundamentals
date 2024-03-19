import re

initial_string = input()
regex = r'(^|(?<=\s))(-?)([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

matches = re.findall(regex, initial_string)

#print(matches)

for element in matches:
    print(f'{element[1]}{element[2]}{element[3]}', end=' ')
