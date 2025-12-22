import random 
from card import Card
from rules import Rules
from LinkedDeque import LinkedDeque

class Deck:
    
    def __init__(self):
        self.numOfDecks = Rules.num_decks
        # INITIALIZING THE DECK
        # Starts as an array to collect all needed cards for the shoe size
        self.suitsAvailable = ["spades", "clubs", "diamonds", "hearts"]
        self.ranksAvailable = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        self.deque = LinkedDeque()


        rankToValueMap = {"ace": [1, 11], "2": [2], "3": [3], "4": [4], "5": [5], "6": [6], "7": [7], "8": [8], "9": [9], 
                          "10": [10], "jack": [10], "queen": [10], "king": [10]}
        
        self.deckArray = []
        for deckNum in range(self.numOfDecks): #amount of decks we will create
            singleDeckArray = []
            for suit in range(len(self.suitsAvailable)):
                for rank in range(len(self.ranksAvailable)):
                    newCard = Card(self.suitsAvailable[suit], self.ranksAvailable[rank], rankToValueMap[self.ranksAvailable[rank]])
                    singleDeckArray.append(newCard)

            self.deckArray += singleDeckArray


        random.shuffle(self.deckArray)

        # Push into an the empty deque for easy push and pop operations
        for i in range(len(self.deckArray)):
             self.deque.pushFront(self.deckArray[i])

    def takeTopCard(self) -> Card:
        return self.deque.popFront()
    
    def peekTopCard(self) -> Card:
        return self.deque.peekFront()
    

    def deckIsEmpty(self) -> bool:
        return self.deque.isEmpty()
    
    def displayDeque(self) -> list:
         currentNode = self.deque.head

         while (currentNode != None):
              currentCard = currentNode.value
              print(currentCard)

              currentNode = currentNode.next

