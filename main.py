import create_game
import print_card
import players
import board
from click import getchar
from os import system


PLAYERS = []
DECK = create_game.deck

while True:
    print('WELCOME TO THE HEARTS GAME')
    print('1. RULES -> PRESS "1"')
    print('2. START -> PRESS "2"')
    print('3. EXIT  -> PRESS OTHER')
    first_choice = input()
    if first_choice == '1':
        _ = system('clear')
        print('Rules:')
        print('CLICK TO CONTINUE...')
        temp = input()
        _ = system('clear')
    elif first_choice == '2':
        _ = system('clear')
        for i in range(1, 5):
            print('WRITE PLAYER {0} NAME'.format(i))
            name = input('NAME: ')
            _ = system('clear')
            print('WRITE PLAYER {0} TYPE (AI OR HUMAN)'.format(i))
            p_type = input('TYPE: ')
            _ = system('clear')
            if p_type.upper() == 'HUMAN':
                new_p = players.HumanPlayer(name, p_type, i)
            else:
                pass
            PLAYERS.append(new_p)
        for i in range(1, 5):
            DECK.shuffle()
            DECK.deal(PLAYERS, i)
            turn = 1
            for g in range(1, 14):
                new_table = board.Table()
                for j in range(1, 5):
                    if PLAYERS[(turn + j - 2) % 4].player_type.upper() == 'HUMAN':
                        pick = 1
                        while True:
                            print(PLAYERS[(turn + j - 2) % 4].name + '\'s DECK')
                            print()
                            print('CHOOSE CARDS USING "," and ".". CLICK "/" TO APPROVE, PRESS "p" TO PRINT THE TABLE')
                            print()
                            print_card.print_deck(PLAYERS[(turn + j - 2) % 4].deck, pick)
                            card_choice = getchar()
                            if card_choice == 'p':
                                _ = system('clear')
                                print_card.print_table(new_table)
                                print('CLICK TO CONTINUE...')
                                temp = input()
                                _ = system('clear')
                            elif card_choice == ',' and pick > 1:
                                pick -= 1
                            elif card_choice == '.' and pick < len(PLAYERS[j - 1].deck):
                                pick += 1
                            elif card_choice == '/':
                                if j == 1:
                                    only_hearts = True
                                    if PLAYERS[(turn + j - 2) % 4].deck[pick - 1].suit == 'Hearts':
                                        for c in PLAYERS[(turn + j - 2) % 4].deck:
                                            if c.suit != 'Hearts':
                                                only_hearts = False
                                                print('YOU CANNOT PICK HEARTS IF YOU STILL HAVE OTHER SUITS')
                                                print('CLICK TO CONTINUE...')
                                                temp = input()
                                                _ = system('clear')
                                                break
                                        if only_hearts:
                                            new_table.winner = PLAYERS[(turn + j - 2) % 4]
                                            new_table.winning_card = PLAYERS[(turn + j - 2) % 4].deck[pick - 1]
                                            new_table.suit = PLAYERS[(turn + j - 2) % 4].deck[pick - 1].suit
                                            new_table.cards.append(PLAYERS[(turn + j - 2) % 4].deck[pick - 1])
                                            new_table.points += PLAYERS[(turn + j - 2) % 4].deck[pick - 1].value
                                            PLAYERS[(turn + j - 2) % 4].deck.pop(pick - 1)
                                            break
                                    else:
                                        new_table.winner = PLAYERS[(turn + j - 2) % 4]
                                        new_table.winning_card = PLAYERS[(turn + j - 2) % 4].deck[pick - 1]
                                        new_table.suit = PLAYERS[(turn + j - 2) % 4].deck[pick - 1].suit
                                        new_table.cards.append(PLAYERS[(turn + j - 2) % 4].deck[pick - 1])
                                        new_table.points += PLAYERS[(turn + j - 2) % 4].deck[pick - 1].value
                                        PLAYERS[(turn + j - 2) % 4].deck.pop(pick - 1)
                                        break
                                else:
                                    if PLAYERS[(turn + j - 2) % 4].deck[pick - 1].suit == new_table.suit:
                                        if PLAYERS[(turn + j - 2) % 4].deck[pick - 1].priority > new_table.winning_card.priority:
                                            new_table.winner = PLAYERS[(turn + j - 2) % 4]
                                            new_table.winning_card = PLAYERS[(turn + j - 2) % 4].deck[pick - 1]
                                        new_table.cards.append(PLAYERS[(turn + j - 2) % 4].deck[pick - 1])
                                        new_table.points += PLAYERS[(turn + j - 2) % 4].deck[pick - 1].value
                                        PLAYERS[(turn + j - 2) % 4].deck.pop(pick - 1)
                                        break
                                    else:
                                        no_cards = True
                                        for c in PLAYERS[(turn + j - 2) % 4].deck:
                                            if c.suit == new_table.suit:
                                                no_cards = False
                                                print('YOU CANNOT PICK THAT CARD')
                                                print('CLICK TO CONTINUE...')
                                                temp = input()
                                                _ = system('clear')
                                                break
                                        if no_cards:
                                            new_table.cards.append(PLAYERS[(turn + j - 2) % 4].deck[pick - 1])
                                            new_table.points += PLAYERS[(turn + j - 2) % 4].deck[pick - 1].value
                                            PLAYERS[(turn + j - 2) % 4].deck.pop(pick - 1)
                                            break
                            _ = system('clear')
                        _ = system('clear')
                        print('CLICK TO CONTINUE...')
                        temp = input()
                        _ = system('clear')

                for p in PLAYERS:
                    if p is new_table.winner:
                        if i < 9:
                            p.round_points -= new_table.points
                            p.round_points -= 4
                            p.points -= new_table.points
                            p.points -= 4
                            if g == 7 or g == 13:
                                p.round_points -= 26
                                p.points -= 26
                        else:
                            pass
                turn = new_table.winner.turn
            print('PLAYERS POINTS:')
            for p in PLAYERS:
                print(p.name + ': ' + str(p.round_points))
                p.round_points = 0
            print('CLICK TO CONTINUE...')
            temp = input()
            _ = system('clear')
    else:
        _ = system('clear')
        break
