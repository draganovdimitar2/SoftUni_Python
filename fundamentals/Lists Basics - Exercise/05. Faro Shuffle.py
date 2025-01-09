deck_of_cards = input().split()
count_of_shuffles = int(input())

for current_shuffle in range(count_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    shuffled_deck = []

    for card_index in range(len(left_part)): # len(right_part)
        shuffled_deck.append(left_part[card_index])
        shuffled_deck.append(right_part[card_index])

    deck_of_cards = shuffled_deck

print(deck_of_cards)