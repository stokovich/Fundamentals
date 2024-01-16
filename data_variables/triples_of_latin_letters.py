n = int(input())

for i in range(n):
    for j in range(n):
        for k in range(n):
            char1 = chr(97 + i)
            char2 = chr(97 + j)
            char3 = chr(97 + k)

            print(f'{char1}{char2}{char3}')