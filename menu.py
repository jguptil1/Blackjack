from rules import Rules

class Menus:

    def __init__(self):
        self.rules = Rules()

    def gameStartMenu(self):
        print("Welcome to Poker!")

    def printTableRules(self):
        print(f"Min Bet: {self.rules.min_bet}")
        print(f"Max Bet: {self.rules.max_bet}")
