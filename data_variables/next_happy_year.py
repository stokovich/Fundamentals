starting_year = int(input())
current_year = starting_year + 1
while True:

    if len(set(str(current_year))) == len(str(current_year)):
        print(current_year)
        break

    current_year += 1