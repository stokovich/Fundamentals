def word_filter():
    new_list = [x for x in initial_list if len(x) % 2 == 0]

    for element in new_list:
        print(element)


initial_list = input().split()
word_filter()