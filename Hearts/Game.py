from Player import Player
from Card import Card
import random

class Game():
    def __init__(self, player_A: Player, player_B: Player, player_C: Player, player_D: Player, cards: list[Card]) -> None:
        self.playerlist = [player_A, player_B, player_C, player_D]
        self.deck = cards
        self.currentRound = 0
        self.current_turn_player_index = 0
        self.rounds = list[Round]
    
    def DealCards(self) -> None:
        random.shuffle(self.deck)
        self.cardcount = 0
        current_player_to_deal = self.playerlist[0]

        # deal shuffled cards in round robin style, add each card to the players' hand
        for index, card in enumerate(self.deck):
            current_player_to_deal = self.playerlist[index % 4]
            current_player_to_deal.hand.append(card)

            # player who gets the 2 of clubs goes first
            if card.name == "2-club":
                current_player_to_deal.is_round_starter = True
                self.current_turn_player_index = index % 4
        

    def Run(self) -> None:
        self.DealCards()

        for i in range(13):
            self.rounds.append(Round())
        

    pass



    # should Round be an internal class???
class Round:
    # every round needs a target suit
    #   a highest deckvalue card
    #   a total point value
    #   to know whether hearts have been broken
    # also pass in the players    
    def __init__(self):
        pass
            