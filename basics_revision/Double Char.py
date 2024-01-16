`while True:
    line = input()
    if line == 'End':
        break
    if line == 'SoftUni':
        continue

    for i in range(len(line)):
        for j in range(2):
            print(line[i], end='')
    print()