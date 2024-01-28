matrix = []
player_won = 0

for i in range(3):
    matrix.append(input().split())

for element in matrix:
    count_1 = element.count('1')
    count_2 = element.count('2')
    if count_1 == 3:
        player_won = 1
        break
    elif count_2 == 3:
        player_won = 2


for i in range(3):
    count_1 = 0
    count_2 = 0
    for j in range(3):
        element = matrix[j][i]
        if element == '1':
            count_1 += 1
        if element == '2':
            count_2 += 1
    if count_1 == 3:
        player_won = 1
        break
    elif count_2 == 3:
        player_won = 2

count_1 = 0
count_2 = 0
for i in range(3):
    element = matrix[i][i]
    if element == '1':
        count_1 += 1
    if element == '2':
        count_2 += 1
    if count_1 == 3:
        player_won = 1
        break
    elif count_2 == 3:
        player_won = 2
        break

count_1 = 0
count_2 = 0
for i in range(3):
    element = matrix[i][2 - i]
    if element == '1':
        count_1 += 1
    if element == '2':
        count_2 += 1
    if count_1 == 3:
        player_won = 1
        break
    elif count_2 == 3:
        player_won = 2
        break

if player_won == 1:
    print('First player won')
elif player_won == 2:
    print('Second player won')
else:
    print('Draw!')
