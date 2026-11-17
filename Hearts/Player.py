from Card import Card

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.match_score = 0
        self.game_score = 0
        
    def take_turn(self, played_cards: list[Card]) -> Card:

        two_of_clubs = next(
            (card for card in self.hand
                if card.rank == "2" and card.suit == "club"),
             None)
        if two_of_clubs is not None:
            self.hand.remove(two_of_clubs)
            return two_of_clubs
        
        else:
            
        # pick a card to play in the round,
        # depending on what's already been played
        