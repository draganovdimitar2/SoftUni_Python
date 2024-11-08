def existence_check(original_deck, card_name):
    if card_name in original_deck:
        return True
    return False

original_deck = input().split(':')
new_deck = []

while True:
    command = input()
    if command == 'Ready':
        break

    command = command.split()
    action = command[0]
    card_name = command[1]
    if action == 'Add':
        if existence_check(original_deck, card_name):
            new_deck.append(card_name)
        else:
            print("Card not found.")
    elif action == 'Insert':
        index = int(command[-1])
        if index in range(len(new_deck)) and existence_check(original_deck, card_name):
            new_deck.insert(index, card_name)
        else:
            print("Error!")
    elif action == 'Remove':
        if card_name in new_deck:
            new_deck.remove(card_name)
        else:
            print("Card not found.")
    elif action == 'Swap':
        second_card_name = command[-1]
        first_card_index = new_deck.index(card_name)
        second_card_name = new_deck.index(second_card_name)
        new_deck[first_card_index], new_deck[second_card_name] = new_deck[second_card_name], new_deck[first_card_index]
    elif action == 'Shuffle':
        new_deck = new_deck[::-1]

print(' '.join(new_deck))
