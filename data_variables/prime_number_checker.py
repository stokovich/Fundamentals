from math import sqrt

number = int(input())

is_prime = True

for num in range(2, int(sqrt(number)) + 1):
    if number % num == 0:
        is_prime = False
        break
print(is_prime)