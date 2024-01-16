n = int(input())
tank_capacity = 255
liters_in = 0

for i in range(n):
    liters = int(input())

    if tank_capacity - liters < 0:
        print('Insufficient capacity!')
    else:
        tank_capacity -= liters
        liters_in += liters

print(liters_in)
