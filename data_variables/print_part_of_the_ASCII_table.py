first_int = int(input())
last_int = int(input())

for i in range(first_int, last_int + 1):
    character = chr(i)
    print(f'{character}', end=' ')