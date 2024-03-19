def follow_grades():
    n = int(input())
    library_grades = {}
    grades_to_remove = []

    for i in range(n):
        student_name = input()
        grade = float(input())

        if student_name not in library_grades.keys():
            library_grades[student_name] = []

        library_grades[student_name].append(grade)

    for key, value in library_grades.items():
        average_grade = sum(value) / len(value)

        if average_grade < 4.50:
            grades_to_remove.append(key)

    for element in grades_to_remove:
        library_grades.pop(element)

    for key,value in library_grades.items():
        average_grade = sum(value) / len(value)
        print(f'{key} -> {average_grade:.2f}')


follow_grades()

