from Player import Player
from Card import Card, Deck
from Round import Round
import random

class Game():
    def __init__(self, player_A: Player, player_B: Player, player_C: Player, player_D: Player) -> None:
        self.playerlist = [player_A, player_B, player_C, player_D]
        self.deck = Deck()
        self.current_turn_player_index = 0
        self.rounds: list[Round] = []
        self.hearts_broken: bool = False
        
    
    def deal_cards(self) -> None:
        self.deck.shuffle()
        self.cardcount = 0

        # deal shuffled cards in round robin style, add each card to the players' hand
        for index, card in enumerate(self.deck):
            current_player_to_deal = self.playerlist[index % len(self.playerlist)]
            current_player_to_deal.hand.append(card)

            # player who gets the 2 of clubs goes first
            if card.rank == "2" and card.suit == "club":
                current_player_to_deal.is_round_starter = True
                self.current_turn_player_index = index % 4
        

    def run(self) -> None:
        self.deal_cards()

        for i in range(13):
            round = Round(self.playerlist, self.current_turn_player_index, self.hearts_broken)
            self.rounds.append(round)

            round.run()
        

    pass


            