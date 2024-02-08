def counter_strike_battles(energy):
    battles_won = 0
    while True:
        curr_line = input()

        if battles_won % 3 == 0 and battles_won != 0:
            energy += battles_won

        if curr_line == 'End of battle':
            print(f'Won battles: {battles_won}. Energy left: {energy}')
            break

        distance = int(curr_line)

        if energy < distance:
            print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
            break

        energy -= distance
        battles_won += 1


initial_energy = int(input())

counter_strike_battles(initial_energy)
