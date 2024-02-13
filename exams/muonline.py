def playing_game(lst: list):
    health = 100
    bitcoins = 0
    curr_room = 1

    for element in lst:
        element_as_list = element.split()
        type_encounter = element_as_list[0]
        points = int(element_as_list[1])
        healed_amount = 0

        if type_encounter == 'potion':
            if points + health > 100:
                healed_amount = 100 - health
                health = 100
            else:
                health += points
                healed_amount = points
            print(f'You healed for {healed_amount} hp.')
            print(f'Current health: {health} hp.')

        elif type_encounter == 'chest':
            bitcoins += points
            print(f'You found {points} bitcoins.')

        else:

            if health <= points:
                print(f'You died! Killed by {type_encounter}.')
                print(f'Best room: {curr_room}')
                break
            else:
                health -= points
                print(f'You slayed {type_encounter}.')

        curr_room += 1

    else:
        print(f'You\'ve made it!')
        print(f'Bitcoins: {bitcoins}')
        print(f'Health: {health}')


initial_list = input().split('|')
playing_game(initial_list)
