def check_students():
    searched_course = ''
    students = {}
    while True:
        curr_line = input()

        if ":" not in curr_line:
            searched_course = curr_line
            break

        curr_line = curr_line.split(':')

        key = curr_line[0] + ' - ' + curr_line[1]
        value = curr_line[2]

        students[key] = value

    searched_course = searched_course.replace('_', ' ')

    for key,value in students.items():
        if value == searched_course:
            print(key)


check_students()

