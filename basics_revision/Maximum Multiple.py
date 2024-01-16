divisor = int(input())
boundary = int(input())
num_found = 0

for number in range(1,boundary + 1):
    if number % divisor == 0:
        num_found = number

print(num_found)