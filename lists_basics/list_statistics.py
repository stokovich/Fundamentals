n = int(input())

positive_list = []
negative_list = []
count_positive = 0
sum_negative = 0

for i in range(n):
    number = int(input())

    if number >= 0:
        positive_list.append(number)
        count_positive += 1

    if number < 0:
        negative_list.append(number)
        sum_negative += number

print(positive_list)
print(negative_list)
print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')