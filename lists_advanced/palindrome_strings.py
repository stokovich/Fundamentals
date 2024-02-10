def find_palindromes(lst: list, word):
    palindromes = []
    for element in lst:
        curr_list = [x for x in element]
        reverse_list = list(curr_list.__reversed__())

        if curr_list == reverse_list:
            palindromes.append(element)

    word_count = palindromes.count(word)

    return palindromes, word_count


initial_list = input().split()
initial_word = input()

final_list, word_counter = find_palindromes(initial_list, initial_word)

print(final_list)
print(f'Found palindrome {word_counter} times')

