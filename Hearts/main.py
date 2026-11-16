import json
from Card import Card


with open("Hearts/deck_52_minimal.json", "r") as file:
    full_card_data = json.load(file)

deck = []

for card in full_card_data:
    deck.append(Card(card["deckvalue"], card["suit"]))

for card in deck:
    print(card.name)






