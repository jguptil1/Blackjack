class Card:

    def __init__(self, suit, value):
        self.value = value
        self.suit = suit


    def value(self) -> int:
        """
        Docstring for value
        
        :param self: the card itself
        :return: returns a list containing integer/s for the value of the card
        :rtype: int
        """
        if self.is_ace():
            return [1, 11]
        elif (self.is_face()):
            return [10]
        else:
            return [int(self.value)]


    def is_ace(self) -> bool:
        if self.value == "ace":
            return True
        else:
            return False
        
    def is_face(self) -> bool:
        if self.value in ["jack", "queen", "king"]:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.value} of {self.suit}'
    
    def __repr__(self):
        return str(self)
    

    
