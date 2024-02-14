def check_plunder(days, daily_plunder, target):
    collected_plunder = 0

    for day in range(1, days + 1):

        collected_plunder += daily_plunder

        if day % 3 == 0:
            collected_plunder += daily_plunder * 0.5

        if day % 5 == 0:
            collected_plunder -= collected_plunder * 0.30

    if collected_plunder >= target:
        print(f'Ahoy! {collected_plunder:.2f} plunder gained.')
    else:
        percent = collected_plunder / target * 100
        print(f'Collected only {percent:.2f}% of the plunder.')


initial_days = int(input())
initial_daily_plunder = int(input())
initial_target = float(input())

check_plunder(initial_days, initial_daily_plunder, initial_target)
