from card import Card

class Hand:

    def __init__(self, betSize: int, card: Card | None = None):
        #construction from split
        self.handArray = []
        self.handValue = 0
        self.aceCount = 0
        if card is not None: 
            self.createdBySplit = True
            self.updateHand(card)
        else:
            self.createdBySplit = False
        self.isDone = False #nothing has happened yet
        self.betSize = betSize
        self.isSoft = False


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
                self.isSoft = True

        self.handValue = currentHandValue


    def updateHand(self, newCard: Card):
        #this will add the new card to the array
        self.handArray.append(newCard)
        # will call updateHandValue
        self.updateHandValue()

    def displayHand(self) -> None:
        for card in self.handArray:
            print(card)
    
    def displayTopCard(self) -> Card:
        return self.handArray[0]


    def removeBottomCardFromHand(self) -> Card:
        if len(self.handArray >= 2):
            card = self.handArray.pop(1)
            return card

    def getHandValue(self) -> int:
        return self.handValue

    def isBlackjack(self) -> bool:
        if self.handValue == 21 and len(self.handArray) == 2:
            self.handState = "done"
            return True
        else:
            return False
    
    def isSoft(self) -> bool:
        return self.isSoft
        
    def isBust(self) -> bool:
        if self.handValue > 21:
            return True
        else:
            return False
    
    def isDone(self)-> bool:
        return self.isDone

    def __len__(self):
        return len(self.handArray)

    def getHandState(self):
        return self.handState
