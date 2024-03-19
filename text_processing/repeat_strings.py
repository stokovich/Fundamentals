def repeat_strings():
    initial_list = input().split()

    for element in initial_list:
        print(element * len(element), end='')


repeat_strings()
