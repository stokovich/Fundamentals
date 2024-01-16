word = input()
final_list = []
for i in range(len(word)):
    if word[i].isupper():
        final_list.append(i)

print(final_list)