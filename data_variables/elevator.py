number_of_people = int(input())
capacity = int(input())

number_full_courses = number_of_people // capacity
people_in_last_course = number_of_people % capacity

if people_in_last_course == 0:
    print(number_full_courses)
else:
    print(number_full_courses + 1)