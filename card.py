import re

class Card:
    SUIT_TO_STRING = {
        1: "s",
        2: "h",
        3: "d",
        4: "c"
    }
    
    RANK_TO_STRING = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K",
        14: "A"
    }
    
    STRING_TO_SUIT = {v:k for k, v in SUIT_TO_STRING.items()}
    STRING_TO_RANK = {v:k for k, v in RANK_TO_STRING.items()}
    
    REPR_RE = re.compile(r'\((.*?)\)')
    
    def __init__(self, rank, suit):
        """
        Create a card. 
        
        rank: int
            [2-14] representing [2-A].
        suit: int 
            [1-4] representing [spades, hearts, diamonds, clubs].
        """
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return "{}{}".format(self.RANK_TO_STRING[self.rank], self.SUIT_TO_STRING[self.suit])

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.rank == other.rank and self.suit == other.suit)
    
    def __hash__(self):
        return hash((self.rank, self.suit))
