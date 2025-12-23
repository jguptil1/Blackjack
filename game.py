import sys
from deck import Deck
from player import Player
from menu import Menus
from hand import Hand
from rules import Rules, SplitPairRule

"""
This class will deal with the game loop logic and will exist until the player becomes bankrupt or until input is quit

"""
class Game:

    def __init__(self, playerName:str, betAmount: int):
        self.gameDeck = Deck()
        self.rules = Rules()
        self.player = Player(rules=self.rules, bankRollAmount=1000, name=playerName)
        self.dealer = Player(rules = self.rules,bankRollAmount=None, name="dealer")
        self.menu = Menus()
        self.roundStatus = "start"
        self.gameResult = None

    def run(self, betSize):
        
        self.menu.gameStartMenu()

        #should be true as long as player doesnt want to quit or player is not bankrupt
        while True:
            print("-------------------------------------------NEW ROUND---------------------------------------------")
            self.menu.printTableRules()
            print(f'Your Current bankroll: {self.player.bankRoll}')
            betAmountInput: int = input("How much would you like to bet: ")

            if betAmountInput.is_integer() and betAmountInput >= self.rules.min_bet and betAmountInput <= self.rules.max_bet:
                self.roundBetAmount  = betAmountInput


            #start of a round (reset hands)
            self.player.resetHands(betChange = self.roundBetAmount)
            self.dealer.resetHands(betChange = None)

            #Initial Deal
            amountOfHands= 1 #the player is always starts with just one hand
        
            dealtCardOne = self.gameDeck.takeTopCard()
            dealtCardTwo = self.gameDeck.takeTopCard()
            dealtCardThree = self.gameDeck.takeTopCard()
            dealtCardFour = self.gameDeck.takeTopCard()

            #building the initial hands
            self.player.hands[0].updateHand(newCard = dealtCardOne)
            self.player.hands[0].updateHand(newCard = dealtCardThree)
            self.dealer.hands[0].updateHand(newCard = dealtCardTwo)
            self.dealer.hands[0].updateHand(newCard = dealtCardFour)

            #showing both of the players cards and the dealers top card
            print() #spacing
            print("Dealers face up card: ")
            self.dealer.displayHands(amountOfCards="one")
            print(f"Dealers up card value: {self.dealer.getDealerFaceValue()}")
            print()
            

            #player turn
            #for each hand
                #while hand not done
                    #compute available action
                    #ask for action (agent or human CLI)
                    #execute action
            

            for i in range(amountOfHands):
                
                #check for blackjack
                if self.player.hands[i].isBlackjack():
                    print("This hand is a blackjack!")
                    self.roundStatus = "naturalBlackjack"
                    continue

                #while the current hand is not done
                while not self.player.hands[i].isDone:
                    print()
                    print("Your cards:")
                    self.player.displayHands(amountOfCards="all")
                    print(f"Your total value: {self.player.hands[0].getHandValue()}")
                    print()
                    print("Avaialable actions:")
                    action = self.player.getPlayerAction()
                    if action == "quit":
                        print("goodbye")
                        sys.quit()

                    if (action == "split"):
                        self.player.hands[i].splitHand()
                        print("You have split") #testing
                        amountOfHands += 1

                    if (action == "hit"):
                        hitCard = self.gameDeck.takeTopCard()
                        self.player.hands[i].updateHand(newCard = hitCard)
                        print("You have hit") #testing
                        
                        #check bust after hit
                        if self.player.hands[i].isBust():
                            print("You have busted!")
                            self.player.hands[i].isDone = True



                    if (action == "double"): #FIXME: this has problems after calling
                        self.player.double(handNum=i) #this only deals with the finances
                        doubleCard = self.gameDeck.takeTopCard()
                        self.player.hands[i].updateHand(newCard=doubleCard)
                        self.player.hands[i].isDone = True
                        print("You have double") #testing
                    if (action == "stand"):
                        self.player.hands[i].isDone = True
                        print("You have stood")
                
            #dealer turn
            #reveal hole card
            print()
            print("Revealing dealers hand:")
            self.dealer.displayHands(amountOfCards="all")
            dealerValue = self.dealer.hands[0].getHandValue()
            print(f"Dealer value {dealerValue}")
            #hit stand rules
            while self.rules.dealer_should_hit(hand_total=self.dealer.hands[0].handValue, is_soft=self.dealer.hands[0].isSoft):
                dealerNewCard = self.gameDeck.takeTopCard()
                self.dealer.hands[0].updateHand(dealerNewCard)

            #settle winner
            #loop through each hand of players and comp with dealer
            for i in range(amountOfHands):
                winner: str = None
                if (self.roundStatus == "naturalBlackjack"):
                    winner = self.player.name
                    #add to bankroll whatever was bet and go with ruleset on blackjack multiplier
                    self.player.addBankRoll((self.player.hands[i].betSize)*self.rules.blackjack_payout)
                elif(self.dealer.hands[0].getHandValue() > self.player.hands[i].getHandValue()):
                    winner = self.dealer.name
                    #take away from bankroll whatever was bet
                    self.player.deductBankRoll(self.player.hands[i].betSize)
                elif (self.player.hands[i].getHandValue() > self.dealer.hands[0].getHandValue()):
                    winner = self.player.name
                    self.player.addBankRoll((self.player.hands[i].betSize)*self.rules.regular_win_payout)


            # compare totals/BJ/Busts/BlackJack payout rules

            #ask playagain?














