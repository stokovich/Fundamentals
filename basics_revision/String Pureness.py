n = int(input())

for i in range(n):
    line = input()
    pure = True
    for j in range(len(line)):
        if line[j] == ',' or line[j] == '.' or line[j] == '_':
            pure = False
            break
    if pure:
        print(f'{line} is pure.')
    else:
        print(f'{line} is not pure!')