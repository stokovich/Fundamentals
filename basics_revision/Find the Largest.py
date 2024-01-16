line = input()
line_as_list = []
new_line = ''

for i in range (len(line)):
    line_as_list.append(line[i])

line_as_list.sort(reverse=True)

#print(line_as_list)

for ele in line_as_list:
    new_line += ele

print(new_line)