def decipher_message():
    word_for_decipher = input()
    decipher_list = [x for x in word_for_decipher]

    while True:
        curr_line = input()

        if curr_line == 'Decode':
            break

        curr_line = curr_line.split('|')
        action = curr_line[0]

        if action == 'Move':
            number_letters = int(curr_line[1])
            #
            # for i in range(number_letters):
            #     decipher_list.append(decipher_list.pop(0))

            word_for_decipher = word_for_decipher[number_letters:] + word_for_decipher[:number_letters]


        elif action == 'Insert':
            index = int(curr_line[1])
            value = curr_line[2]

            # decipher_list.insert(index, value)

            word_for_decipher = word_for_decipher[:index] + value + word_for_decipher[index:]

        elif action == 'ChangeAll':
            string = curr_line[1]
            replacement = curr_line[2]

            # word_for_replacement = ''.join(decipher_list)

            word_for_decipher = word_for_decipher.replace(string, replacement)

            # decipher_list = [x for x in word_for_replacement]

            # decipher_list[:] = [x if x != string else replacement for x in decipher_list]

    # word_for_decipher = ''.join(decipher_list)

    print(f'The decrypted message is: {word_for_decipher}')


decipher_message()


