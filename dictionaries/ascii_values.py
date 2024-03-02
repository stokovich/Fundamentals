def make_dict():
    initial_list = input().split(', ')

    ascii_dict = {x: ord(x) for x in initial_list}

    print(ascii_dict)


make_dict()
