import re

text = input()
regex = r'(?:^|(?<=\s))[a-zA-Z][\w.-]+@[a-zA-Z][a-zA-Z-]+\.[a-zA-Z]+\.?[a-zA-Z]*\b'

matches = re.findall(regex, text)

# print(matches)

for element in matches:
    print(element)
