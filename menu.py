from rules import Rules

class Menus:

    def __init__(self):
        self.rules = Rules()

    def gameStartMenu():
        print("Welcome to Poker!")

    def printTableRules(self):
        print(f"Min Bet: {self.rules.minBet}")
        print(f"Max Bet: {self.rules.maxBet}")
