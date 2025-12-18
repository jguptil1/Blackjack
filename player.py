from hand import Hand
from rules import Rules

class Player:

    def __init__(self, name, bankRollAmount, rules:Rules):
        self.rules = rules
        self.name = name
        self.hands = [Hand()] #FIXME: for now there is no splitting ATM so a single hand is fine, with splitting we will need to create mutliple hands
        self.bankRoll = bankRollAmount


    #helper function
    def determine_split(self, hand) -> bool:
        if (self.rules.allow_split and len(hand.cards) == 2 and len(hand) + 1 <= self.rules.max_hands and hand.handState != "done" and self.bankRoll > hand.bet):
            #further determination based on specific rule set

            # are the two cards the same rank and is ruleset sameRank? 
            if (self.rules.split_pair_rule == "same_rank" and (hand.handArray[0].rank == hand.handArray[1].rank)):
                return True

            #are the two cards the same value and is ruleset sameValue?
            elif (self.rules.split_pair_rule == "same_value" and (hand.handArray[0].value == hand.handArray[1].value)):
                return True
            
            else:
                return False
            
        else:
            return False

    #helper function
    def determine_double(self, hand) -> bool:
        if(self.rules.allow_double and len(hand) == 2 and self.bankRoll > hand.bet): 
            #need to do a rule check on if the hand is a result of a split
            if (hand.createdBySplit and self.rules.double_after_split_allowed):
                return True
        else:
            return False


    def avaialable_actions(self, hand) -> list:
        """
        This returns a list determing if split eligable and double eligable
        """
        avaialable_actions = []
        
        #DETERMINING SPLIT from helper function
        if (self.determine_split()):
            avaialable_actions += "split"

        #DETERMINING DOUBLE from helper function
        if (self.determine_double()):
            avaialable_actions += "double"

        #DETERMINING STAND
        avaialable_actions += "stand"

        #DETERMINING HIT
        if (hand.value < 21):
            avaialable_actions += "hit"

        return avaialable_actions


    def getPlayerAction(self) -> str:
        """
        This method verifies correct input val and returns controlled string vals
        """
        actions = self.avaialable_actions()
        #print(f'Avaialble Actions: {for action in actions: print(action)}') #FIXME: I know that this is wrong
        player_action = input("What action would you like to do: ").lower()
        if player_action == "hit": return "hit"
        elif player_action == "stand": return "stand"
        elif player_action == "double": return "double"
        elif player_action == "split": return "split"
        else: raise ValueError("Invalid Input")
    

    def displayHands(self):
        for hand in self.hands:
            hand.displayHand()


        



