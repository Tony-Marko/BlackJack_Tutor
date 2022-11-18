from classes.card import Card
from classes.deck import Deck
class Dealer:
    def __init__(self):
        self.name = "The Dealer"
        self.hand = []
        self.hand_val = 0

    def showfirsthand(self):
        print("The Dealer is showing:")
        Card.card_info(self.hand[1])
        for x in self.hand:
            self.hand_val += x.point_val
        if len(self.hand) == 2 and self.hand_val == 21:
            print("Dealer has 21!")
            return self.hand_val
        return self.hand_val


    def showhand(self):
        for x in self.hand:
            Card.card_info(x)
        # for x in self.hand:
        #     self.hand_val += x.point_val
        # return self.hand_val
            

    def action(self, bicycle):
        print(f"Dealer's turn")
        Dealer.showhand(self)
        if self.hand_val < 17:
            print("Dealer hits")
            self.hand_val = Deck.hit(bicycle, self)
            if self.hand_val > 21:
                print (f"Dealer BUST with {self.hand_val}!")
                return self.hand_val
            else: 
                print(f"Dealer has {self.hand_val}")
                Dealer.action(self, bicycle)
        elif self.hand_val > 16 or self.hand_val < 22:
            print(f"Dealer stands with {self.hand_val}")
            return self.hand_val
        

    