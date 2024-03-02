def find_occurrences():
    initial_text = input()
    occurrences = {}

    for char in initial_text:
        if char == ' ':
            continue

        if char not in occurrences.keys():
            occurrences[char] = 0

        occurrences[char] += 1

    for char, count in occurrences.items():
        print(f'{char} -> {count}')


find_occurrences()
