budget = float(input())
price_flour = float(input())

recipe_eggs = 1
recipe_flour = 1
recipe_milk = 0.25

number_loaves = 0
number_eggs = 0

price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25

while True:
    current_price = 0
    current_price = price_eggs + price_flour + recipe_milk * price_milk
    if budget - current_price <= 0:
        break
    budget -= current_price
    number_loaves += 1
    number_eggs += 3

    if number_loaves % 3 == 0:
        number_eggs -= number_loaves - 2

print(f'You made {number_loaves} loaves of Easter bread! Now you have {number_eggs} eggs and {budget:.2f}BGN left.')
