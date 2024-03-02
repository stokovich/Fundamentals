from math import floor


def calculate_factory_production():
    biscuits_per_day = int(input())
    count_of_workers = int(input())
    biscuits_competing_factory = int(input())

    produced_biscuits = 0

    for day in range(1, 31):

        if day % 3 == 0:
            produced_biscuits += floor((biscuits_per_day * count_of_workers) * 0.75)
        else:
            produced_biscuits += biscuits_per_day * count_of_workers

    print(f'You have produced {produced_biscuits} biscuits for the past month.')

    biscuit_difference = produced_biscuits - biscuits_competing_factory

    percentage_difference = biscuit_difference / biscuits_competing_factory * 100

    if percentage_difference < 0:
        print(f'You produce {abs(percentage_difference):.2f} percent less biscuits.')
    else:
        print(f'You produce {percentage_difference:.2f} percent more biscuits.')


calculate_factory_production()