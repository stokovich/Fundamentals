def sorting_function(x):
    return sorted(x)


initial_list = [int(x) for x in input().split()]

result = list(sorting_function(initial_list))

print(result)