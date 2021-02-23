class Player:
    def __init__(self, name, player_type, turn):
        self.name = name
        self.player_type = player_type
        self.turn = turn
        self.deck = []
        self.round_points = 0
        self.points = 0


class HumanPlayer(Player):
    def sort_deck(self):
        hearts = []
        spades = []
        club = []
        diamond = []
        for c in self.deck:
            if c.suit == 'Hearts':
                hearts.append(c)
            elif c.suit == 'Spades':
                spades.append(c)
            elif c.suit == 'Club':
                club.append(c)
            elif c.suit == 'Diamond':
                diamond.append(c)
        hearts = sorted(hearts, key=lambda x: x.priority)
        spades = sorted(spades, key=lambda x: x.priority)
        club = sorted(club, key=lambda x: x.priority)
        diamond = sorted(diamond, key=lambda x: x.priority)
        self.deck = club + diamond + spades + hearts
