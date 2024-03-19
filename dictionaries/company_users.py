def company_id_sorter():
    library_company = {}
    while True:
        curr_line = input()

        if curr_line == 'End':
            break

        curr_line = curr_line.split(' -> ')

        company_name = curr_line[0]
        id_number = curr_line[1]

        if company_name not in library_company.keys():
            library_company[company_name] = []

        if id_number in library_company[company_name]:
            continue
        else:
            library_company[company_name].append(id_number)

    for key,value in library_company.items():
        print(f'{key}')

        for element in value:
            print(f'-- {element}')


company_id_sorter()
