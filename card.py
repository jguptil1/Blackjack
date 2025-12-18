class Card:

    def __init__(self, suit, rank, value):
        self.valueList = value #will always be list with 1 or two elements within
        self.rank = rank #will always be str
        self.suit = suit


    def value(self) -> list:
        """
        Docstring for value
        
        :param self: the card itself
        :return: returns an integer for the value of the card
        :rtype: int
        """
        return self.valueList


    def is_ace(self) -> bool:
        if self.rank == "ace":
            return True
        else:
            return False
        
    def is_face(self) -> bool:
        if self.rank in ["jack", "queen", "king"]:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __repr__(self):
        return str(self)
    

    
