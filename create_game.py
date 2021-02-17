import board


suits = ('Spades', 'Hearts', 'Diamond', 'Club')
names = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'Jack': 9, 'Queen': 10, 'King': 12, 'Ace': 12}
cards = []

for name in names.keys():
    for suit in suits:
        value = None
        if name.isdigit() or name == 'Ace':
            value = 0
        else:
            value = 13
        if suit == 'Hearts' and name == 'King':
            value = 69
        elif suit == 'Hearts':
            value += 4

        new_card = board.Card(name, value, suit, names[name])
        cards.append(new_card)

deck = board.Deck(cards)


