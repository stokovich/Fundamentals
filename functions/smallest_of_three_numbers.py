def find_smallest_number(a, b, c):
    smallest_list = [a, b, c]
    min_number = min(smallest_list)
    return min_number


first_num = int(input())
second_num = int(input())
third_num = int(input())

result = find_smallest_number(first_num, second_num, third_num)

print(result)


