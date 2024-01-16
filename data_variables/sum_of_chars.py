n = int(input())
sum_of_characters = 0

for i in range(n):
    character = input()
    sum_of_characters += ord(character)

print(f'The sum equals: {sum_of_characters}')