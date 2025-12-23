from game import Game
from rules import Rules
from menu import Menus


"""
This class is for testing purposes and is a way for me to test the game function
While main looks at this class now, it will eventually be taken over by the agent class (hopefully lol)

"""



class HumanCLI:

    def __init__(self):
        self.game = Game(playerName="Jack", betAmount = self.getBetSize())
        self.rules = Rules()
        self.menus = Menus()
        
    def run(self):
        self.game.run()


    #helper
    def getBetSize(self) -> int:
        self.menus.printTableRules()
        cliBetSize = int(input("how much would you like to bet: "))

        if cliBetSize > self.rules.max_bet:
            raise Exception("Error: bet size too big")
        elif cliBetSize < self.rules.min_bet:
            raise Exception("Error: bet size too small")
        return cliBetSize
    