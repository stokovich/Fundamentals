n = int(input())
is_balanced = True
is_open_brackets = False
is_close_brackets = False

for i in range(n):
    line = input()

    if line == '(' and is_open_brackets is False:
        is_open_brackets = True
    elif line == '(' and is_open_brackets is True:
        is_balanced = False
        break
    elif line == ')' and is_open_brackets is True:
        is_balanced = True
        is_open_brackets = False
    elif line == ')' and is_open_brackets is False:
        is_balanced = False
        break

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

