import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')
else:
    print(f'There are {len(deck)} cards in the deck.')

print('Dealing ...')

hand = []
while len(hand) < 5:
    hand.append(deck.pop(random.randint(0, len(deck)-1)))
else:
    print(f'There are {len(deck)} cards in the deck.')
    print('Player has the following cards in their hand:')
    print(hand)
