cards = input().split(':')
deck = []

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Ready':
        break

    elif command == 'Add':
        card_name = tokens[1]
        if card_name in cards:
            deck.append(card_name)
        else:
            print("Card not found.")

    elif command == 'Insert':
        card_name = tokens[1]
        index = int(tokens[2])
        if 0 <= index < len(deck) and card_name in cards:
            deck.insert(index, card_name)
        else:
            print("Error!")

    elif command == 'Remove':
        card_name = tokens[1]
        if card_name in deck:
            deck.remove(card_name)
        else:
            print("Card not found.")

    elif command == 'Swap':
        card_one = tokens[1]
        card_two = tokens[2]
        index_one = 0
        index_two = 0
        for cards in deck:
            if cards == card_one:
                break
            index_one += 1
        for cards in deck:
            if cards == card_two:
                break
            index_two += 1
        if index_one < index_two:
            deck[index_one], deck[index_two] = deck[index_two], deck[index_one]
        else:
            deck[index_two], deck[index_one] = deck[index_one], deck[index_two]
    elif command == 'Shuffle':
        deck.reverse()
print(' '.join(deck))
