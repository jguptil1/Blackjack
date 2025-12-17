import random 
from card import Card
from LinkedDeque import LinkedDeque

class Deck:
    
    def __init__(self, numOfDecks):
        # INITIALIZING THE DECK
    
        # Starts as an array to collect all needed cards for the shoe size
        self.numDecks = numOfDecks
        self.suitsAvailable = ["spades", "clubs", "diamonds", "hearts"]
        self.valuesAvailable = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        
        self.deckArray = []
        for deckNum in range(numOfDecks): #amount of decks we will create
            singleDeckArray = []
            for suit in range(len(self.suitsAvailable)):
                for value in range(len(self.valuesAvailable)):
                    newCard = Card(self.suitsAvailable[suit], self.valuesAvailable[value])
                    singleDeckArray.append(newCard)

            self.deckArray.append(singleDeckArray)

        # Shuffle in place
        random.shuffle(self.deckArray)

        # Push into an empty stack for easy push and pop operations
        self.deque = LinkedDeque()
        for i in range(len(self.deckArray)):
             self.deque.pushFront(self.deckArray[i])
    
    def displayDeque(self):
         currentNode = self.deque.head

         while (currentNode != None):
              currentCard = currentNode.value
              print(currentCard)

              currentNode = currentNode.next