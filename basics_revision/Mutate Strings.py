first_string = input()
second_string = input()

for i in range(len(first_string)):
    if first_string[i] == second_string[i]:
        continue
    char_original = first_string[i]
    char_switch = second_string[i]
    first_string = first_string[:i] + second_string[i] + first_string[i+1:]
    print(first_string)