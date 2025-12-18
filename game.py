from deck import Deck
from hand import Hand
from rules import Rule

gameDeck = Deck(1)
rules = Rule()
gameDeck.displayDeque()


print(f'Game Deck is Empty: {gameDeck.deckIsEmpty()}')
print(f'Top card: {gameDeck.peekTopCard()}') #this will just print the reference to the object

#creating a hand with the two top cards
hand = Hand()
card1 = gameDeck.takeTopCard()
card2 = gameDeck.takeTopCard()
hand.updateHand(card1)
hand.updateHand(card2)

print(f'current hand value: {hand.getHandValue()}')
hand.displayHand()











