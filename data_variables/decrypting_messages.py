key = int(input())
n = int(input())

for i in range(n):
    curr_char = input()
    new_char = chr(ord(curr_char) + key)
    print(new_char, end='')
