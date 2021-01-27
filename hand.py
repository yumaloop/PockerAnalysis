import numpy as np

class Hand():
    def __init__(self, cards):
        """
        cards: list
            list of Card() class objects.
        """
        self.cards = cards
        
    def evaluate(self):
        hand_score, hand_name = HandEvaluater(self.cards).evaluate()
        return hand_score, hand_name
    
    def __repr__(self):
        return ''.join([repr(c) for c in self.cards])


class HandEvaluater():
    def __init__(self, cards):
        """
        cards: list
            list of Card() class objects.
        """
        suit_set = set()
        rank_list = []
        for card in cards:
            suit_set.add(card.suit)
            rank_list.append(card.rank)
        rank_list.sort()
        
        self.suit_set = suit_set
        self.rank_arr = np.array(rank_list)        
        self.duplicate_rank_arr = np.array([x for x in set(rank_list) if rank_list.count(x) > 1])
        
    def evaluate(self):
        if self.is_StraightFlush():
            hand_score = 9
            hand_name = "Straight Flush"
        elif self.is_FourCard():
            hand_score = 8
            hand_name = "FourCard"
        elif self.is_FullHouse():
            hand_score = 7
            hand_name = "FullHouse"
        elif self.is_Flush():
            hand_score = 6
            hand_name = "Flush"
        elif self.is_Straight():
            hand_score = 5
            hand_name = "Straight"
        elif self.is_ThreeCard():
            hand_score = 4
            hand_name = "ThreeCard"
        elif self.is_TwoPair():
            hand_score = 3
            hand_name = "TwoPair"
        elif self.is_OnePair():
            hand_score = 2
            hand_name = "OnePair"
        elif self.is_HighCard():
            hand_score = 1
            hand_name = "HighCard"

        return hand_score, hand_name
        
    def is_StraightFlush(self):
        if self.is_Flush() and self.is_Straight():
            return True
        else:
            return False
        
    def is_FourCard(self):
        if len(self.duplicate_rank_arr) == 1 and len(set(self.rank_arr)) == 2:
            return True
        else:
            return False
        
    def is_FullHouse(self):
        if len(self.duplicate_rank_arr) == 2 and len(set(self.rank_arr)) == 2:
            return True
        else:
            return False
        
    def is_Flush(self):
        if len(self.suit_set) == 1:
            return True
        else:
            return False
        
    def is_Straight(self):
        if np.all(np.diff(self.rank_arr) == 1):
            return True
        else:
            return False
        
    def is_ThreeCard(self):
        if len(self.duplicate_rank_arr) == 1 and len(set(self.rank_arr)) == 3:
            return True
        else:
            return False
    
    def is_TwoPair(self):
        if len(self.duplicate_rank_arr) == 2 and len(set(self.rank_arr)) == 3:
            return True
        else:
            return False
    
    def is_OnePair(self):
        if len(self.duplicate_rank_arr) == 1 and len(set(self.rank_arr)) == 4:
            return True
        else:
            return False
        
    def is_HighCard(self):
        if len(self.duplicate_rank_arr) == 0 and len(set(self.rank_arr)) == 5:
            return True
        else:
            return False
