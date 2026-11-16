from Card import Card

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.score = 0
        self.is_round_starter = False
        
    def TakeTurn(played_cards: list[Card]) -> Card:
        
        # pick a card to play in the round,
        # depending on what's already been played
        
    #def StartRound(bool heartsbroken) -> Card:
        
        # pick a card to play to start the next round,
        # depending on whether hearts have been broken or not
        pass