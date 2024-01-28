initial_list = input().split()
execution_step = int(input())
# integer_list = [int(x) for x in initial_list]
working_list = initial_list
executed_list = []
i = 0
step = 1

while len(working_list) > 0:
    element = working_list[i]
    if step == execution_step:
        executed_list.append(element)
        working_list.pop(i)
        step = 1
    else:
        step += 1
        i += 1
    if i > len(working_list) - 1:
        i = 0

print('[', end='')
print(','.join(executed_list), end='')
print(']')



