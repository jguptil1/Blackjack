from card import Card

class Hand:

    def __init__(self, betSize):
        #empty hand constructor
        self.handArray = [] #array full of Card Objects
        self.handValue = 0
        self.aceCount = 0
        self.createdBySplit = False
        self.handState = None #nothing has happened yet
        self.betSize =  betSize

    def __init__(self, card:Card, betSize):
        #construction from split
        self.handArray = []
        self.handValue = 0
        self.aceCount = 0
        self.updateHand(card)
        self.createdBySplit = True
        self.handState = None #nothing has happened yet
        self.betSize = betSize


    #helper function
    def updateAceCount(self):
        currAceCount = 0
        for card in self.handArray:
            values = card.value()
            if len(values) > 1:
                currAceCount += 1
        self.aceCount = currAceCount

    
    #helper function
    def updateHandValue(self):
        #Step 0: get ace count updated
        self.updateAceCount()
        #Step 1: treat Aces initially as a value of 1
        currentHandValue = 0 
        for card in self.handArray:
            currentHandValue += card.value()[0]

        
        #Step 2: stepping through the aces and upgrading as allowable
        for i in range(self.aceCount):
            if currentHandValue + 10 <= 21:
                #upgrading one of the aces
                currentHandValue += 10

        self.handValue = currentHandValue


    def updateHand(self, newCard: Card):
        #this will add the new card to the array
        self.handArray.append(newCard)
        # will call updateHandValue
        self.updateHandValue()


    def displayHand(self) -> None:
        for card in self.handArray:
            print(card)


    def popCardFromHand(self) -> Card:
        topCard = self.handArray[0]
        self.handArray[0] = self.handArray[1] #moving second card to head pos
        return topCard



    def getHandValue(self) -> int:
        return self.handValue

    def isBlackjack(self) -> bool: #terminal
        self.handState = "done"
        return self.handValue == 21
    
    def isSoft(self) -> bool:
        self.handState = "playable"
        return self.aceCount > 0
        
    def isBust(self): #terminal
        self.handState = "done"
        return self.handValue > 21
