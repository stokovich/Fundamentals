def check_for_validity(a):
    validity_list = [False, False, False]

    # First check for 6-10 chars
    if 6 <= len(a) <= 10:
        validity_list[0] = True

    # Second check for only letters and digits
    for element in a:
        if 48 <= ord(element) <= 57 or 65 <= ord(element) <= 90 or 97 <= ord(element) <= 122:
            validity_list[1] = True
        else:
            validity_list[1] = False
            break
    # Third check for at least 2 digits
    counter = 0
    for element in a:
        if 48 <= ord(element) <= 57:
            counter += 1
    if counter >= 2:
        validity_list[2] = True

    # returns the validation list
    return validity_list


# working phase
password_for_checking = input()
validation_list = check_for_validity(password_for_checking)

if validation_list[0] is True and validation_list[1] is True and validation_list[2] is True:
    print('Password is valid')
else:
    if validation_list[0] is False:
        print('Password must be between 6 and 10 characters')
    if validation_list[1] is False:
        print('Password must consist only of letters and digits')
    if validation_list[2] is False:
        print('Password must have at least 2 digits')


