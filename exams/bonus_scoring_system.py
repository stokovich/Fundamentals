from math import ceil


def find_max_bonus():
    number_students = int(input())
    number_lectures = int(input())
    additional_bonus = int(input())
    max_bonus = 0
    max_lectures = 0

    for i in range(number_students):
        student_lectures = int(input())

        total_bonus = student_lectures / number_lectures * (5 + additional_bonus)

        if total_bonus > max_bonus:
            max_bonus = total_bonus
            max_lectures = student_lectures

    print(f'Max Bonus: {ceil(max_bonus)}.')
    print(f'The student has attended {max_lectures} lectures.')


find_max_bonus()
