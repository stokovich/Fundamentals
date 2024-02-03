initial_list = [int(x) for x in input().split()]

result = list(filter(lambda x: x % 2 == 0, initial_list))

print(result)