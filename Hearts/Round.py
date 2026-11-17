from Card import Card
from Player import Player


class Round:
    def __init__(self, players: list[Player], starting_player_index: int, hearts_broken: bool):
        self.starting_player_index = starting_player_index
        self.players = players[starting_player_index:] + players[:starting_player_index]
        self.hearts_broken = hearts_broken
        self.cards_placed_down: list[(Card, Player)] = []
        self.target_suit: str = ""
        self.lead_card: Card
        self.total_point_value_of_round = 0
        pass

    def run(self) -> None:
        # each player takes their turn
        for count, player in self.players:
            new_card = player.take_turn(self.cards_placed_down, self.target_suit, count)
            self.cards_placed_down.append((new_card, player))

            # the first turn sets the target suit and is the starting lead_card
            if len(self.cards_placed_down) < 2:
                self.target_suit = new_card.suit
                self.lead_card = new_card

            # not first turns:
            else:
                # the highest card that meets the target suit becomes lead_card
                if new_card.suit == self.target_suit and new_card.deck_value > self.lead_card:
                    self.lead_card = new_card

            # hearts add 1 point, queen of spades adds 13 points
            if new_card.suit == "heart":
                self.total_point_value_of_round += 1
            if new_card.rank == "Q" and new_card.suit == "spade":
                self.total_point_value_of_round += 13

            
        pass

    def get_lead_player(self) -> Player:
        