def find_occurrences():
    initial_list = input().split()
    duplicates_dict = {}

    for element in initial_list:
        if element.lower() in duplicates_dict.keys():
            duplicates_dict[element.lower()] += 1
        else:
            duplicates_dict[element.lower()] = 1

    for key, value in duplicates_dict.items():
        if value % 2 != 0:
            print(key, end=' ')


find_occurrences()
