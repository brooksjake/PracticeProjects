from Player import Player
from Card import Card, Deck
from Round import Round
import random

class Match():
    def __init__(self, player_A: Player, player_B: Player, player_C: Player, player_D: Player) -> None:
        self.playerlist = [player_A, player_B, player_C, player_D]
        self.deck = Deck()
        self.current_turn_player_index = 0
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

        # run 13 rounds
        for round_number in range(13):
            round = Round(self.playerlist, self.current_turn_player_index, self.hearts_broken, round_number)
            round.run()
            self.hearts_broken = round.get_hearts_broken()

        self.apply_game_points()

    def apply_game_points(self) -> None:
        
        if self.moon_shot_by() is not None:
            self.moon_shot_by.game_score -= 26
        else:
            for player in self.playerlist:
                player.game_score += player.match_score
                player.match_score = 0

    def moon_shot_by(self) -> Player:
        for player in self.playerlist:
            if player.match_score > 25: return player
        return None


            