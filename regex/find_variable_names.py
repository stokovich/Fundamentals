import re

text = input()
regex = r'(?<=\s_)[a-zA-Z0-9]+\b'

matches = re.findall(regex, text)

print(','.join(matches))
