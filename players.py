class Player:
    def __init__(self, name, player_type, turn):
        self.name = name
        self.player_type = player_type
        self.turn = turn
        self.deck = []
    
    
class HumanPlayer(Player):
    pass