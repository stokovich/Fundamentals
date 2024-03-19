def caesar_cipher():
    initial_string = input()
    encrypted_string = ''

    for char in initial_string:
        index = ord(char) + 3
        new_substring = chr(index)
        encrypted_string += new_substring

    print(encrypted_string)


caesar_cipher()

