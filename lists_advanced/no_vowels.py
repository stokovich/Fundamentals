word = input()

final_list = [x for x in word if x.lower() not in ['a', 'o', 'u', 'e', 'i']]

list_as_string = ''.join(final_list)

print(list_as_string)