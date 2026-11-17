from Card import Card
from Player import Player


class Round:
    def __init__(self, players: list[Player], starting_player_index: int, hearts_broken: bool, round_count: int):
        self.starting_player_index = starting_player_index
        self.players = players[starting_player_index:] + players[:starting_player_index]
        self.hearts_broken = hearts_broken
        self.round_count = round_count
        self.played_cards: list[tuple[Card, Player]] = []
        self.lead_suit: str = ""
        self.lead_turn_index: int = 0
        self.round_points = 0
        pass

    def run(self) -> None:
        # each player takes their turn
        for turn_count, player in self.players:
            new_card = player.take_turn(self.played_cards, self.lead_suit, turn_count, self.round_count)
            self.played_cards.append((new_card, player))

            if new_card.suit == "heart":
                self.hearts_broken = True

            # the first turn sets the target suit and is the starting lead_turn_index
            if len(self.played_cards) < 2:
                self.lead_suit = new_card.suit

            # not first turns:
            else:
                # the highest card that meets the target suit becomes lead_card
                if new_card.suit == self.lead_suit and new_card.deck_value > self.lead_turn_index:
                    self.lead_turn_index = turn_count

        self.count_points()
        self.apply_points_to_lead_player()

    def get_lead_player(self) -> Player:
        return self.players[self.lead_turn_index]

    def count_points(self) -> None:
        # hearts add 1 point, queen of spades adds 13 points
        for card, _ in self.played_cards:
            if card.suit == "heart":
                self.round_points += 1
            if card.rank == "Q" and card.suit == "spade":
                self.round_points += 13

    def apply_points_to_lead_player(self) -> None:
        if self.round_points > 0:
            self.get_lead_player().match_scorescore += self.round_points

    def get_hearts_broken(self) -> bool: return self.hearts_broken