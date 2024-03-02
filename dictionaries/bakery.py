def create_dictionary():
    initial_list = input().split()
    final_dict = {}

    for i in range(0, len(initial_list), 2):
        key = initial_list[i]
        value = int(initial_list[i + 1])

        final_dict[key] = value

    return final_dict


print(create_dictionary())