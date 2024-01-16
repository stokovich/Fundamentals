line_of_words = input()

string_to_list = line_of_words.split(', ')

string_to_list.reverse()

#print(string_to_list)

if string_to_list[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for i in range(len(string_to_list)):
        if string_to_list[i] == 'wolf':
            print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')
            break