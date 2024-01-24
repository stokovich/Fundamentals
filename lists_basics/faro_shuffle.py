initial_string = input()
number_of_shuffles = int(input())

deck = initial_string.split(' ')

shuffled_deck = []

half_of_deck_length = len(deck) // 2

for j in range(number_of_shuffles):
    shuffled_deck = []
    for i in range(half_of_deck_length):
        shuffled_deck.append(deck[i])
        shuffled_deck.append(deck[i + half_of_deck_length])
    deck = shuffled_deck

print(shuffled_deck)