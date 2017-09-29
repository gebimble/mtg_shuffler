import json


card_names_list = ['thoughtseize', 'inquisition of kozilek',
                   'dismember', 'liliana of the veil',
                   "raven's crime",
                   'wrench mind', 'the rack', 'shrieking affliction',
                   'smallpox', 'funeral charm', 'swamp',
                   'marsh flats',
                   'urborg, tomb of yawgmoth', 'mutavault',
                   'fatal push']

quantities = [4, 4, 1, 3, 4, 4, 4, 4, 4, 2, 12, 4, 4, 4, 2]

cards = {}

for i, name in enumerate(card_names_list):
    cards[i] = {'name': card_names_list[i],
                'quantity': quantities[i]}

data = json.dumps(cards, indent=4)

with open('deck.txt', 'w') as f:
    json.dump(cards, f)
