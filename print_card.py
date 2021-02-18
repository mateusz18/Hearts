def print_deck(deck, pick):
    for i in range(len(deck)):
        print('-' * 10, end='') if i + 1 == pick else print(' ' * 10, end='')
    print()
    for i in range(len(deck)):
        n = 8 - len(deck[i].name)
        print('| ' + deck[i].name, end=' '*n) if i + 1 == pick else print('-' * 10, end='')
    print('-')
    for i in range(len(deck)):
        n = 8 - len(deck[i].name)
        m = 8 - len(deck[i].suit)
        print('| ' + deck[i].suit, end=' '*m) if i + 1 == pick else print('| ' + deck[i].name, end=' '*n)
    print('|')
    for i in range(len(deck)):
        n = 8 - len(deck[i].suit)
        print('|', end=' '*9) if i + 1 == pick else print('| ' + deck[i].suit, end=' '*n)
    print('|')
    for _ in range(4):
        for i in range(len(deck)):
            print('|', end=' '*9)
        print('|')
