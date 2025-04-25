import random

class Card: #card instance
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    #Things this class will need to do:
        #1. iniitialize the deck will all possible combinations
        #2. shuffle the deck
        #3. deal the top card
        #4. count remaining cards (check to see if empty)

    card_options = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.cards = self.create_deck()
    
    def create_deck(self):
        deck = [] #empty deck to append
        for i in self.card_options:
            for j in self.suits:
                card = Card(i,j) #creating a new card instance with the appropriate values
                deck.append(card)
        return deck
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
        print('You have shuffled the deck') #just for testing purposes

    def deal_card(self):
        if len(self.cards) > 0: #theres atleast one card to deal
            dealt_card = self.cards[0]
            self.cards.pop(0) #removes the card from the list
            print(len(self.cards)) #tells us how many cards remain in the deck
        return dealt_card
        #should return the top card and remove that card from the deck entirely



def main():
    deck = Deck() #creates a deck
    deck.shuffle_deck() #shuffles the deck
    deck.deal_card() #deals a card


main()



    

