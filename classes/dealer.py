from classes.card import Card
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