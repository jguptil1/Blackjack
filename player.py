from hand import Hand
from rules import Rules, SplitPairRule

class Player:

    def __init__(self, name, bankRollAmount, rules:Rules):
        self.rules = rules
        self.name = name
        self.hands = [Hand()]
        self.bankRoll = bankRollAmount
        self.amountOfSplits = 0


    #PLAYER ACTION MANAGEMENT

    #helper function
    def determine_split(self, hand) -> bool:
        # Rule + timing + state + bankroll + max-hands checks
        if not self.rules.allow_split:
            return False
        if len(hand.handArray) != 2:
            return False
        if hand.isDone:
            return False
        if self.bankRoll < hand.betSize:
            return False
        if len(self.hands) + 1 > self.rules.max_hands:
            return False

        # Pair check
        if self.rules.split_pair_rule is SplitPairRule.SAME_RANK:
            return hand.handArray[0].rank == hand.handArray[1].rank

        # Pair check (same-value) — not implemented yet
        if self.rules.split_pair_rule is SplitPairRule.SAME_VALUE:
            return False

        return False

    #helper function
    def determine_double(self, hand) -> bool:
        if(self.rules.allow_double and len(hand) == 2 and self.bankRoll >= hand.betSize): 
            #need to do a rule check on if the hand is a result of a split
            if (hand.createdBySplit and not self.rules.double_after_split_allowed):
                return False
            else:
                return True
        else:
            return False

    def avaialable_actions(self, hand) -> list:
        """
        This returns a list determing if split eligable and double eligable
        """
        avaialable_actions = []
        
        #DETERMINING SPLIT from helper function
        if (self.determine_split(hand)):
            avaialable_actions.append("split")

        #DETERMINING DOUBLE from helper function
        if (self.determine_double(hand)):
            avaialable_actions.append("double")

        #DETERMINING STAND
        avaialable_actions.append("stand")

        #DETERMINING HIT
        if (not hand.isDone() and hand.handValue < 21):
            avaialable_actions.append("hit")

        return avaialable_actions

    def getPlayerAction(self) -> str:
        """
        This method verifies correct input val and returns controlled string vals
        """
        for hand in self.hands:

            actions = self.avaialable_actions(hand)
            
            #printing each of the available actions
            for action in actions:
                print(action)

            player_action = input("What action would you like to do: ").lower()

            while True:
                #valid input check
                if player_action.lower() in actions:
                    return player_action.lower()


    #BANKROLL MANAGEMENT

    def addBankRoll(self, amount:int) -> None:
        self.bankRoll += amount

    def deductBankRoll(self, amount: int) -> None:
        self.bankRoll -= amount

    def printBankRoll(self):
        print(self.bankRoll)

    #HAND MANAGEMENT

    def double(self, hand) -> None: #FIXME
        #bankroll needs to be decremented and the betSize needs to be doubled
        

    def splitHand(self, hand) -> None:
        if self.determine_split():
            self.amountOfSplits += 1
            topCard = hand.removeBottomCardFromHand()
            newHand = Hand(card=topCard, betSize=hand.betSize)
            self.bankRoll -= newHand.betSize
            self.hands.append(newHand)

    def displayHands(self):
        for hand in self.hands:
            hand.displayHand()

    def resetHands(self):
        self.hands = [Hand()]

        



