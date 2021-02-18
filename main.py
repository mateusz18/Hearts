import create_game
import print_card
import players
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
        system('clear')
        print('Rules:')
        print('CLICK TO CONTINUE...')
        temp = input()
        system('clear')
    elif first_choice == '2':
        system('clear')
        for i in range(1, 5):
            print('WRITE PLAYER {0} NAME'.format(i))
            name = input('NAME: ')
            system('clear')
            print('WRITE PLAYER {0} TYPE (AI OR HUMAN)'.format(i))
            p_type = input('TYPE: ')
            system('clear')
            if p_type == 'HUMAN':
                new_p = players.HumanPlayer(name, p_type, i)
            else:
                pass
            PLAYERS.append(new_p)
        for i in range(1, 5):
            DECK.shuffle()
            DECK.deal(PLAYERS, i)
            for g in range(1, 14):
                for j in range(1, 5):
                    if PLAYERS[j - 1].player_type == 'HUMAN':
                        pick = 1
                        while True:
                            print(PLAYERS[j - 1].name + '\'s DECK')
                            print()
                            print('CHOOSE CARDS USING "," and ".". CLICK "/" TO APPROVE')
                            print()
                            print_card.print_deck(PLAYERS[j - 1].deck, pick)
                            card_choice = getchar()
                            if card_choice == ',' and pick > 1:
                                pick -= 1
                            elif card_choice == '.' and pick < len(PLAYERS[j - 1].deck):
                                pick += 1
                            elif card_choice == '/':
                                break
                            system('clear')
                        PLAYERS[j - 1].deck.pop(pick - 1)
                        system('clear')
                        print('CLICK TO CONTINUE...')
                        temp = input()
                        system('clear')
            
    else:
        system('clear')
        break

   