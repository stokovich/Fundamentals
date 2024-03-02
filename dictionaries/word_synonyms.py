def find_synonym():
    n = int(input())
    dictionary = {}
    for i in range(n):
        word = input()
        synonym = input()

        if word not in dictionary.keys():
            dictionary[word] = []

        dictionary[word].append(synonym)

    for word, synonym in dictionary.items():
        synonym_as_string = ', '.join(synonym)
        print(f'{word} - {synonym_as_string}')


find_synonym()
