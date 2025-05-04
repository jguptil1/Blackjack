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
        self.value = 0
    
    def add_card(self, card):
        self.hand.append(card)

    def show_full_hand(self): #will show all cards in terminal
        print(f'{self.name}: ')
        for i in self.hand:
            print(i)
    
    def show_dealer_card(self):
        if self.name == 'Dealer': #just for safe measure that the instance is an actual dealer
            print(f'{self.name}: {self.hand[0]}')
        else:
            print('error')
            
    def calc_hand_value(self):
        hand_value = 0
        aces = 0
        for i in self.hand:
            #Card values can either be Ace, 1-10, or Jack, Queen, King
            if i.value in ['Jack', 'Queen', 'King']: #face card values
                hand_value += 10
            elif i.value == 'Ace':
                hand_value += 11
                aces += 1
            elif i.value.isdigit():
                hand_value += int(i.value) #we simply just add the value of the card to the total hand value
        if aces>1:
            hand_value -= 11
        #print(f'Current Hand Value: {hand_value}')
        return hand_value
    
    def print_hand_value(self):
        print(f'Current hand value: {self.value}')

    def hit_or_stand(self):
        #should return 'hit' or 'stand'
        ##Dealer has automated rules, no input
        if self.name == 'Dealer': #Should follow dealer rules on playing until atleast a hand value of 17
            if self.value > 17:
                return 'stand'
            else:
                return 'hit'
        else: #Regular player logic
            user_input = input('Would you like to hit or stand? (h/s): ')
            if user_input.lower() == 'h':
                return 'hit'
            elif user_input.lower() == 's':
                return 'stand'
            else:
                return 'bad input'
            

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

    inital_hand_value = player_instance.calc_hand_value()
    print(f'Current Hand Value: {inital_hand_value}')


    ### Bulk game logic ###

    ##Start with the player

    ## if hit, add a card and ask again until they bust or stand
    while True:
        player_decision = player_instance.hit_or_stand()
        if player_decision.lower() == 'hit':
            # Need to add a card to the hand. 
            player_instance.add_card(deck_instance.deal_card())
            #display the updated hand.
            player_instance.show_full_hand()
            #displaye the updated hand value
            new_hand_value = player_instance.calc_hand_value()
            print(f'New Hand Value: {new_hand_value}')

            #if they bust:
            if int(new_hand_value) > 21:
                print('You have busted. End of Hand')
                break
            else: 
                continue
                
        elif player_decision.lower() == 'stand':
            pass
            #This needs development
            #should show the dealers full hand (need to add this method to the player class)
            #should run the hit_or_stand method for the dealer instance



main()



    

