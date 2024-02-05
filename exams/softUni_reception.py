def calculate_time_needed():
    first_hours = int(input())
    second_hours = int(input())
    third_hours = int(input())
    students_number = int(input())
    processed_students_per_hour = first_hours + second_hours + third_hours
    hours = 0

    while True:
        if hours % 4 == 0 and hours != 0:
            hours += 1
            continue

        if students_number <= 0:
            break

        students_number -= processed_students_per_hour
        hours += 1

    return print(f'Time needed: {hours}h.')


calculate_time_needed()
