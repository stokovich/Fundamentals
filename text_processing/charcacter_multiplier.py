def multiplier():
    initial_list = input().split()
    total_sum = 0
    min_size = 0
    max_size = 0
    str1 = initial_list[0]
    str2 = initial_list[1]

    if len(str1) >= len(str2):
        min_size = len(str2)
        max_size = len(str1)
    else:
        min_size = len(str1)
        max_size = len(str2)

    for i in range(min_size):
        total_sum += ord(str1[i]) * ord(str2[i])

    for j in range(min_size, max_size):
        if len(str1) == max_size:
            total_sum += ord(str1[j])
        else:
            total_sum += ord(str2[j])

    print(total_sum)


multiplier()
