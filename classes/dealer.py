from classes.card import Card
from classes.deck import Deck
class Dealer:
    def __init__(self):
        self.hand = []

    def showfirsthand(self):
        print("The Dealer is showing:")
        Card.card_info(self.hand[1])
        hand_val = 0
        for x in self.hand:
            hand_val += x.point_val
        if len(self.hand) == 2 and hand_val == 21:
            print("Dealer has 21!")
        return hand_val


    def showhand(self):
        for x in self.hand:
            Card.card_info(x)
        hand_val = 0
        for x in self.hand:
            hand_val += x.point_val
        return hand_val
            

    def action(self, bicycle):
        print(f"Dealer's turn")
        hand_val = Dealer.showhand(self)
        if hand_val < 17:
            print("Dealer hits")
            hand_val = Deck.hit(bicycle, self)
            if hand_val > 21:
                print ("BUST!")
                return
            else: 
                print("Dealer has {hand_val}")
                Dealer.action(self, bicycle)
        elif hand_val < 17 or hand_val < 22:
            print("Dealer stands with {hand_val}")
            return
        

    