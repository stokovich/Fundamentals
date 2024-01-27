my_energy = 100
my_coins = 100

my_list = input().split("|")

for element in my_list:
    initial_list = element.split('-')
    event_ingredient = initial_list[0]
    number = int(initial_list[1])
    energy_gained = 0

    if event_ingredient == 'rest':
        if my_energy + number > 100:
            energy_gained = 100 - my_energy
        else:
            energy_gained = number
        my_energy += energy_gained
        print(f'You gained {energy_gained} energy.')
        print(f'Current energy: {my_energy}.')

    elif event_ingredient == 'order':
        if my_energy - 30 >= 0:
            my_coins += number
            my_energy -= 30
            print(f'You earned {number} coins.')
        else:
            my_energy += 50
            print(f'You had to rest!')
    else:
        if my_coins >= number:
            my_coins -= number
            print(f'You bought {event_ingredient}.')
        else:
            print(f'Closed! Cannot afford {event_ingredient}.')
            break
else:
    print(f'Day completed!')
    print(f'Coins: {my_coins}')
    print(f'Energy: {my_energy}')
