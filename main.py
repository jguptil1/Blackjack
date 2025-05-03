import random

class Card: #card instance
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    #Things this class will need to do:
        #1. iniitialize the deck wilth all possible combinations
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

    #should return the top card and remove that card from the deck entirely
    def deal_card(self):
        if len(self.cards) > 0: #theres atleast one card to deal
            dealt_card = self.cards[0]
            self.cards.pop(0) #removes the card from the list
            cards_remaining = (len(self.cards)) #tells us how many cards remain in the deck
        else:
            self.cards = self.create_deck()

        return dealt_card
        
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_card(self, card):
        self.hand.append(card)

    def show_full_hand(self): #will show all cards in terminal
        for i in self.hand:
            print(f'{self.name}: {i}')
    
    def show_dealer_card(self):
        if self.name == 'Dealer': #just for safe measure that the instance is an actual dealer
            print(f'{self.name}: {self.hand[0]}')
        else:
            print('error')
            
    def calc_hand_value(self):
        pass

    def hit_or_stand():
        pass



def main(): #controller of a hand of poker
    
    deck_instance = Deck() #creates a deck
    deck_instance.shuffle_deck() #shuffles the deck
    player_instance = Player(name='Player')
    dealer_instance = Player(name='Dealer')


    # creating the first hand for the player and dealer
    for i in range(2):
        dealt_card = deck_instance.deal_card()
        player_instance.add_card(dealt_card)
        dealt_card = deck_instance.deal_card()
        dealer_instance.add_card(dealt_card)

    #showing the dealers face up card
    dealer_instance.show_dealer_card()

    #showing the cards in the hand, only the first for the dealer
    player_instance.show_full_hand()
    

    

main()



    

