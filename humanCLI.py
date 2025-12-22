from game import Game


"""
This class is for testing purposes and is a way for me to test the game function
While main looks at this class now, it will eventually be taken over by the agent class (hopefully lol)

"""


class HumanCLI:

    def __init__(self):
        self.game = Game(playerName="Jack")
        
    def run(self):
        #need to add more to interact
        self.game.run()

        