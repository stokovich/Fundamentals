def substring():
    working_string = input()
    main_string = input()

    while working_string in main_string:
        main_string = main_string.replace(working_string, '')

    return main_string


print(substring())
