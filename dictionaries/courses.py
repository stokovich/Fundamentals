def check_courses():
    library_courses = {}

    while True:
        curr_line = input()

        if curr_line == 'end':
            break

        curr_line = curr_line.split(' : ')

        course = curr_line[0]
        student_name = curr_line[1]

        if course not in library_courses.keys():
            library_courses[course] = []

        library_courses[course].append(student_name)

    for course, student_name in library_courses.items():
        print(f'{course}: {len(student_name)}')

        for element in student_name:
            print(f'-- {element}')


check_courses()