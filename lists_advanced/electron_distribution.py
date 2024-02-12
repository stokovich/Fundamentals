def electron_distribution(number):
    shell_position = 1
    shells = []
    while True:
        shell_capacity = 2 * shell_position ** 2

        if shell_capacity < number:
            shells.append(shell_capacity)
            number -= shell_capacity
        else:
            shells.append(number)
            break

        shell_position += 1

    print(shells)


initial_number = int(input())

electron_distribution(initial_number)
