from deck import Deck
from player import Player
from menu import Menus
from hand import Hand
from rules import Rules, SplitPairRule

"""
This class will deal with the game loop logic and will exist until the player becomes bankrupt or until input is quit

"""
class Game:

    def __init__(self, playerName:str):
        self.gameDeck = Deck()
        self.rules = Rules()
        self.player = Player(rules=self.rules, bankRollAmount=1000, name=playerName)
        self.dealer = Player(rules = self.rules,bankRollAmount=None, name="dealer")
        self.menu = Menus()

    def run(self):
        
        self.menu.gameStartMenu()
        self.menu.printTableRules()
        self.player.printBankRoll()

    
        #should be true as long as player doesnt want to quit or player is not bankrupt
        while True:
            #start of a round (reset hands)
            self.player.resetHands()
            self.dealer.resetHands()

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
            self.player.displayHands(playerOrDealer="all")
            self.dealer.displayHands(playerOrDealer="one")

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
                    continue

                #while the current hand is not done
                while not self.player.hands[i].isDone():
                    action = self.player.getPlayerAction()
                    if (action == "split"):
                        self.player.hands[i].splitHand()
                    if (action == "hit"):
                        hitCard = self.gameDeck.takeTopCard()
                        self.player.hands[i].updateHand(newCard = hitCard)
                    if (action == "double"):
                        self.player.double(handNum=i) #this only deals with the finances
                        doubleCard = self.gameDeck.takeTopCard()
                        self.player.hands[i].updateHand(newCard=doubleCard)
                        self.player.hands[i].isDone = True
                    if (action == "stand"):
                        self.player.hands[i].isDone = True
                
            #dealer turn
            #reveal hole card
            self.dealer.displayHands(amountOfCards="all")
            #hit stand rules
            while self.rules.dealer_should_hit():
                dealerNewCard = self.gameDeck.takeTopCard()
                self.dealer.hands[0].updateHand(dealerNewCard)

            #settle

            # compare totals/BJ/Busts/BlackJack payout rules


            #ask playagain?














