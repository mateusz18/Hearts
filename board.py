from random import shuffle


class Card:
    def __init__(self, name, value, suit, priority):
        self.name = name
        self.value = value
        self.suit = suit
        self.priority = priority


class Deck:
    def __init__(self, cards):
        self.cards = cards
    
    def shuffle(self):
        shuffle(self.cards)

    def deal(self, players, turn):
        for card in self.cards:
            players[turn - 1].deck.append(card)
            turn += 1
            if turn == 5:
                turn = 1
    

class Table:
    def __init__(self):
        self.cards = []
        self.suit = None
        self.winner = None
        self.winning_card = None
        self.points = 0
