import re

sentence = input()
word = input()

regex = f'\\b{word}\\b'

matches = re.findall(regex, sentence, flags=re.I)

print(len(matches))
