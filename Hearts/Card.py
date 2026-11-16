

class Card():
    def __init__(self, deckvalue: int, suit: str) -> None:

            # ensure correct inputs
        if deckvalue < 2 or deckvalue > 14:
            raise ValueError("Invalid deckvalue: " + str(deckvalue))
        if suit not in ["spade","heart","club","diamond"]:
            raise ValueError("Invalid suit: " + suit)

        self.deckvalue = deckvalue
        self.suit = suit
        
            # assign facecard name
        if self.deckvalue == 11: self.rank = "J"
        elif self.deckvalue == 12: self.rank = "Q"
        elif self.deckvalue == 13: self.rank = "K"
        elif self.deckvalue == 14: self.rank = "A"
        else: self.rank = str(deckvalue)
        self.name = f"{self.rank}-{self.suit}"

        self.pointvalue = 0

        # assign hearts with 1 point, but the Queen of Spades with 13 points
        if self.suit == "heart":
            self.pointvalue = 1
        if self.rank == "Q" and self.suit == "spade":
            self.pointvalue = 13

            