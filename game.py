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
        self.deale = Player(rules = self.rules,bankRollAmount=None, name="dealer")
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
            amountOfHands= 1
        
            dealtCardOne = self.gameDeck.takeTopCard()
            dealtCardTwo = self.gameDeck.takeTopCard()
            dealtCardThree = self.gameDeck.takeTopCard()
            dealtCardFour = self.gameDeck.takeTopCard()
            #building the initial hands
            self.player.Hands[0].updateHand(newCard = dealtCardOne)
            self.player.Hands[0].updateHand(newCard = dealtCardThree)
            self.dealer.Hands[0].updateHand(newCard = dealtCardTwo)
            self.dealer.Hands[0].updateHand(newCard = dealtCardFour)

            #player turn
            #for each hand
                #while hand not done
                    #compute available action
                    #ask for action (agent or human CLI)
                    #execute action

            for i in range(amountOfHands):
                #while the current hand is not done
                while not self.player.hands[i].isDone():
                    action = self.player.getPlayerAction()
                    if (action == "split"):
                        self.player.hands[i].splitHand()
                    if (action == "hit"):
                        self.player.hands[i].isDone = True
                    if (action == "double"):
                        self.player.hands[i].()
                        #should immediately end this hand, ie cant get another card
                    if (action == "stand"):
                
            #delaer turn
            #reveal hole card
            #hit stand rules


            #settle
            # compare totals/BJ/Busts/BlackJack payout rules

            #ask playagain?













