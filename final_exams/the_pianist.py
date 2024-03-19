def collect_pieces():
    n = int(input())
    information_pieces = dict()

    for i in range(n):
        curr_piece = input().split('|')
        information_pieces[curr_piece[0]] = [curr_piece[1], curr_piece[2]]

    while True:
        curr_line = input()

        if curr_line == 'Stop':
            break

        curr_line = curr_line.split('|')

        action = curr_line[0]

        if action == 'Add':
            piece = curr_line[1]
            composer = curr_line[2]
            key = curr_line[3]

            if piece in information_pieces.keys():
                print(f'{piece} is already in the collection!')
            else:
                information_pieces[piece] = [composer, key]
                print(f'{piece} by {composer} in {key} added to the collection!')

        elif action == 'Remove':
            piece = curr_line[1]

            if piece in information_pieces.keys():
                information_pieces.pop(piece)
                print(f'Successfully removed {piece}!')
            else:
                print(f'Invalid operation! {piece} does not exist in the collection.')

        elif action == 'ChangeKey':
            piece = curr_line[1]
            new_key = curr_line[2]

            if piece in information_pieces.keys():
                information_pieces[piece][1] = new_key
                print(f'Changed the key of {piece} to {new_key}!')
            else:
                print(f'Invalid operation! {piece} does not exist in the collection.')

    for piece,value in information_pieces.items():
        composer = value[0]
        key = value[1]

        print(f'{piece} -> Composer: {composer}, Key: {key}')


collect_pieces()
