def check_for_palindrome(a):
    working_list = []
    for element in a:
        working_list.append(element)
    reversed_list = list(reversed(working_list))
    if working_list == reversed_list:
        return True
    else:
        return False


initial_list = input().split(', ')


for element in initial_list:
    print(f'{check_for_palindrome(element)}')

