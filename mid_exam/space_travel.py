def space_travel():
    initial_string = input().split('||')
    fuel = int(input())
    ammunition = int(input())

    for element in initial_string:
        curr_list = element.split()

        if curr_list[0] == 'Titan':
            print(f'You have reached Titan, all passengers are safe.')
            break

        command = curr_list[0]
        value = int(curr_list[1])

        if command == 'Travel':

            if fuel >= value:
                fuel -= value
                print(f'The spaceship travelled {value} light-years.')
            else:
                print(f'Mission failed.')
                break

        elif command == 'Enemy':

            if ammunition >= value:
                ammunition -= value
                print(f'An enemy with {value} armour is defeated.')
            else:
                consumed_fuel = value * 2
                if fuel >= consumed_fuel:
                    fuel -= consumed_fuel
                    print(f'An enemy with {value} armour is outmaneuvered.')
                else:
                    print(f'Mission failed.')
                    break

        elif command == 'Repair':
            fuel += value
            ammunition += value * 2
            print(f'Ammunitions added: {value * 2}.')
            print(f'Fuel added: {value}.')


space_travel()
