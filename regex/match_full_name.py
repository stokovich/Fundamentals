import re

names = input()
regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
valid_names = re.findall(regex, names)

string_output = ' '.join(valid_names)

print(string_output)