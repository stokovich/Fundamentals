def check_perfect_number(num):
    divisors_list = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors_list.append(i)

    if sum(divisors_list) / 2 == num :
        return True
    else:
        return False


number = int(input())
is_perfect = check_perfect_number(number)

if is_perfect:
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')

