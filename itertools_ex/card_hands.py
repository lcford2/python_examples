import itertools
# Get all possible 2 card hands
# Adapted from: https://pybit.es/itertools-examples.html

cards = [str(i) for i in range(2, 11)] + list("JQKA")
suits = "S D C H".split()

all_cards = [f"{suit}{card}" for suit, card in itertools.product(suits, cards)]

for i in itertools.combinations(all_cards, 2):
    print(i)
