from classes.card import Card
class Dealer:
    def __init__(self):
        self.hand = []

    def showfirsthand(self):
        print("The Dealer is showing:")
        Card.card_info(self.hand[1])

    def showhand(self):
        for x in self.hand:
            Card.card_info(x)