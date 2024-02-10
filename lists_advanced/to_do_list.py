def tasks_list():
    tasks = []
    while True:
        curr_line = input()

        if curr_line == 'End':
            break

        tasks.append(curr_line)

    return tasks


unordered_tasks = tasks_list()

ordered_tasks = sorted(unordered_tasks, key=lambda x: int(x.split('-')[0]))

final_tasks = list(map(lambda x: x.split('-')[1], ordered_tasks))

print(final_tasks)