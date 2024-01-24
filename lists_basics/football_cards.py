my_string = input()

team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

my_list = my_string.split(" ")

for element in my_list:
    curr_list = element.split("-")
    # print(curr_list)
    if len(team_A) < 7 or len(team_B) < 7:
        break

    if curr_list[0] == 'A':
        if int(curr_list[1]) not in team_A:
            continue
        else:
            team_A.remove(int(curr_list[1]))
    if curr_list[0] == 'B':
        if int(curr_list[1]) not in team_B:
            continue
        else:
            team_B.remove(int(curr_list[1]))


print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')

if len(team_A) < 7 or len(team_B) < 7:
    print(f'Game was terminated')

# print(team_A)
# print(team_B)