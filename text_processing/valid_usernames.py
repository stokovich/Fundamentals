def check_usernames():
    initial_list = input().split(', ')

    for username in initial_list:
        len_ok = False
        chars_ok = False

        if 3 <= len(username) <= 16:
            len_ok = True

        for char in username:
            if (not 65 <= ord(char) <= 90) and (not 97 <= ord(char) <= 122) and (char != '-') and (char != '_')\
                  and (not 48 <= ord(char) <= 57):
                break
        else:
            chars_ok = True

        if len_ok and chars_ok:
            print(username)


check_usernames()
