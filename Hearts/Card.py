

class Card():
    def __init__(self, deckvalue: int, suit: str) -> None:

            # ensure correct inputs
        if deckvalue < 2 or deckvalue > 14:
            raise ValueError("Invalid deckvalue: " + str(deckvalue))
        if suit not in ["spade","heart","club","diamond"]:
            raise ValueError("Invalid suit: " + suit)

        self.deck_value = deckvalue
        self.suit = suit
        
            # assign facecard name
        if self.deck_value == 11: self.rank = "J"
        elif self.deck_value == 12: self.rank = "Q"
        elif self.deck_value == 13: self.rank = "K"
        elif self.deck_value == 14: self.rank = "A"
        else: self.rank = str(deckvalue)
        self.name = f"{self.rank}-{self.suit}"

        self.point_value = 0

        # assign hearts with 1 point, but the Queen of Spades with 13 points
        if self.suit == "heart":
            self.point_value = 1
        if self.rank == "Q" and self.suit == "spade":
            self.point_value = 13

    # is it worth making this Deck a separate class? (should it be internal?)
    # or would it be better to simply make a list of cards called deck in main.py?
import json
import random
class Deck():
    def __init__(self):
        with open("Hearts/deck_52_minimal.json", "r") as file:
            full_card_data = json.load(file)
        self.cards = []
        for card in full_card_data:
            self.cards.appedn(Card(card["deckvalue"], card["suit"]))
        pass
    def shuffle(self):
        random.shuffle(self.cards)
    
            