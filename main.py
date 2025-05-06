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
        print('Dealer has shuffled the deck') #just for testing purposes

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
        self.value = self.calc_hand_value()

    def show_full_hand(self): #will show all cards in terminal
        print(f'{self.name}: ')
        for i in self.hand:
            print(f'- {i}')
    
    def show_dealer_card(self):
        if self.name == 'Dealer': #just for safe measure that the instance is an actual dealer
            print('Dealer: ')
            print(f'- {self.hand[0]}')

            
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
class Screen:
    ## To be developed

    ## Should be able to return various screens that I can access to give out to the user
    ## End Goal is to simplify the code within main or the game class if it has been refactored over

    ## Desired output look for a hand:
        #Dealer Hand Example: 

        # =======================  #line 1
        # |     DEALER'S HAND    | #line 2
        # |  [10♠] [Hidden]      | #line 3
        # |  Total:              | #line 4
        # =======================  #line 4

        #Player Hand Example:

        # =======================
        # |     PLAYER'S HAND    |
        # |  [8♦] [5♣]           |
        # |  Total: 13           |
        # =======================

    def __init__(self, name, value, hand):
        self.name = name #screen name, will be helpful for dileniated between the players screen and the dealers screen
        self.hand = hand
        self.value = value

    def print_screen(self):

        #Still need to implement: 
            #need to figure out left and right borders
            #total works
            #cards prints 'None'

        length = 23 #initializing to 23 as the base width of the screen, can be adapted if need be
        full_title = str(self.name) + "'s Hand"
        print('='*length) #line 1: top border
        print(f'{full_title:^21}') #line 2: title line
        print(f'{self.hand}') #line 3: Cards
        print(f'Total: {self.value}') #line 4: total line




class Game:
    ## To be developed

    ## Will be refactoring most of the current code from the main function into this class to allow for instances of a game.
    ## The idea is to allow for a string of hands to be played back to back until the user no longer wants to play. 


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
    dealer_instance.show_dealer_card() #will eventually be updated to the new screen
    

    #showing the cards in the hand, only the first for the dealer
    player_inital_hand = player_instance.show_full_hand() #old way, needs to be replaced
    print(player_inital_hand)

    initial_hand_value = player_instance.calc_hand_value()
    
    '''
    Continue implementing below
    This is where I began implementing the new screen class to test the features
    '''


    player_screen = Screen(name='Player', value= initial_hand_value, hand=player_inital_hand)
    player_screen.print_screen()
    
    player_blackjack = False #should stay false unless they get 21 off the rip. 
    if initial_hand_value == 21:
        print('You have blackjack! You win!')
        player_blackjack = True
    else: 
        print(f'Your Initial Hand Value: {initial_hand_value}')


    ### Bulk game logic ###

    ## Player Logic First as they have first move

    ## if hit, add a card and ask again until they bust or stand
    continue_hand = True
    while continue_hand and not(player_blackjack): #will continue the hand as long as it is true and the player hasn't already got blackjack. 
        player_decision = player_instance.hit_or_stand()
        if player_decision.lower() == 'hit':
            # Need to add a card to the hand. 
            print('-'*20)
            print('You have decided to hit')
            player_instance.add_card(deck_instance.deal_card())
            #display the updated hand.
            print()
            dealer_instance.show_dealer_card()
            print('\n')
            player_instance.show_full_hand()
            print('\n')
            #displaye the updated hand value
            new_hand_value = player_instance.calc_hand_value()
            print(f'You have a new hand value: {new_hand_value}')
            print('\n')

            #if they bust:
            if int(new_hand_value) > 21:
                print('You have busted. End of Hand')
                continue_hand = False
            else: 
                continue
             
        elif player_decision.lower() == 'stand': 
            print()
            print('You have decided to stand')
            print('\n')
            
            print('Dealers Turn')
            print('-'*20)
            print('Revealing the Dealers Full Hand: ')
            dealer_instance.show_full_hand()
            print('\n')

            pre_hit_or_stand_deal_val = dealer_instance.calc_hand_value()
            print(f"Dealer's hand value: {pre_hit_or_stand_deal_val}")

            continue_dealer_hand = True
            while continue_dealer_hand: #Dealer's Turn Logic
                dealer_decision = dealer_instance.hit_or_stand()
                

                if dealer_decision == 'hit':
                    print(f'Dealer has to: {dealer_decision}')
                    #need to add a card to dealer hand
                    new_card = deck_instance.deal_card()
                    dealer_instance.add_card(new_card)
                    dealer_instance.show_full_hand()
                    deal_hand_val = dealer_instance.calc_hand_value()
                    print('\n')
                    print(f'Dealer New Hand Value: {deal_hand_val}')
                    print(f'Your Hand Value: {player_instance.calc_hand_value()}')
                    
                    if deal_hand_val == 21:
                        print('Dealer has won.')
                        continue_hand = False
                        break
                    elif deal_hand_val > 21:
                        print('Dealer has busted. You win.')
                        continue_hand = False
                        continue_dealer_hand = False
                else:
                    #dealer has reached at least 17 and we need to determine who won
                    dealer_hand_val = dealer_instance.calc_hand_value()
                    #print(dealer_hand_val)

                    ## Determine winner by comparison
                    if player_instance.calc_hand_value() > dealer_instance.calc_hand_value():
                        print('You have a better hand.')
                        print('You win!')
                    elif player_instance.calc_hand_value() < dealer_instance.calc_hand_value():
                        print('Dealer has a better hand.')
                        print('Dealer wins.')
                    else:
                        print('Push')

                    continue_hand = False
                    continue_dealer_hand = False
            

main()



    

