def print_deck(deck):
    print()
    print('-' * 10 * len(deck) + '-')
    for card in deck:
        n = 8 - len(card.name)
        print('| ' + str(card.name), end=' ' * n)
    print('|')
    for card in deck:
        n = 8 - len(card.suit)
        print('| ' + str(card.suit), end=' ' * n)
    print('|')
    for i in range(5):
        for i in range(len(deck) + 1):
            print('|         ', end='')
        print()
