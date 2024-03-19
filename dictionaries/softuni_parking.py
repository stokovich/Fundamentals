def parking_system():
    n = int(input())
    parking_lot = {}

    for i in range(n):
        curr_line = input().split()
        movement = curr_line[0]

        if movement == 'register':
            username = curr_line[1]
            license_plate = curr_line[2]

            if username in parking_lot.keys():
                print(f'ERROR: already registered with plate number {parking_lot[username]}')
            else:
                parking_lot[username] = license_plate
                print(f'{username} registered {license_plate} successfully')

        if movement == 'unregister':
            username = curr_line[1]

            if username not in parking_lot.keys():
                print(f'ERROR: user {username} not found')
            else:
                parking_lot.pop(username)
                print(f'{username} unregistered successfully')

    for username, plate in parking_lot.items():
        print(f'{username} => {plate}')


parking_system()



