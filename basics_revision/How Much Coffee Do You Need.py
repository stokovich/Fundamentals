num_coffee = 0

while True:
    line = input()

    if line == 'END':
        break

    if line.lower() == 'coding' or line.lower() == 'dog' or line.lower() == 'cat' or line.lower() == 'movie':
        if line.islower():
            num_coffee += 1
        else:
            num_coffee += 2
    else:
        continue

if num_coffee > 5:
    print('You need extra sleep')
else:
    print(num_coffee)