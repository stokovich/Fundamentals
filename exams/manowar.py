def outcome_of_battle():
    pirate_ship = input().split('>')
    warship = input().split('>')
    max_health = int(input())

    pirate_ship = list(map(int, pirate_ship))
    warship = list(map(int, warship))

    while True:
        curr_line = input()

        if curr_line == 'Retire':
            sum_pirate_ship = sum(pirate_ship)
            sum_warship = sum(warship)

            print(f'Pirate ship status: {sum_pirate_ship}')
            print(f'Warship status: {sum_warship}')

            break

        curr_line = curr_line.split()

        if curr_line[0] == 'Fire':
            index = int(curr_line[1])
            damage = int(curr_line[2])

            if not 0 <= index < len(warship):
                continue
            else:
                warship[index] -= damage

                if warship[index] <= 0:
                    print(f'You won! The enemy ship has sunken.')
                    break

        elif curr_line[0] == 'Defend':
            start_index = int(curr_line[1])
            end_index = int(curr_line[2])
            damage = int(curr_line[3])

            if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):

                for i in range(start_index, end_index + 1):
                    pirate_ship[i] -= damage

                if pirate_ship[i] <= 0:
                    print(f'You lost! The pirate ship has sunken.')
                    break

            else:
                continue

        elif curr_line[0] == 'Repair':
            index = int(curr_line[1])
            health = int(curr_line[2])

            if 0 <= index < len(pirate_ship):
                pirate_ship[index] += health

                if pirate_ship[index] > max_health:
                    pirate_ship[index] = max_health

            else:
                continue

        elif curr_line[0] == 'Status':
            count = sum(h / max_health < 0.2 for h in pirate_ship)
            print(f'{count} sections need repair.')


outcome_of_battle()

