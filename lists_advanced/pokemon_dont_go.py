def pokemon_game():
    sequence = input().split()
    sequence = list(map(int, sequence))
    removed_elements = []

    while True:
        if len(sequence) == 0:
            print(sum(removed_elements))
            break

        index = int(input())

        if 0 <= index < len(sequence):
            removed_element = sequence.pop(index)
        elif index < 0:
            removed_element = sequence.pop(0)
            sequence.insert(0, sequence[-1])
        else:
            removed_element = sequence.pop(-1)
            sequence.append(sequence[0])

        removed_elements.append(removed_element)

        for i in range(len(sequence)):

            if sequence[i] <= removed_element:
                sequence[i] += removed_element
            else:
                sequence[i] -= removed_element


pokemon_game()
