n = int(input())

positive_list = []
negative_list = []


for i in range(n):
    number = int(input())

    if number >= 0:
        positive_list.append(number)

    if number < 0:
        negative_list.append(number)

count_positive = len(positive_list)
sum_negative = sum(negative_list)

print(positive_list)
print(negative_list)
print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')