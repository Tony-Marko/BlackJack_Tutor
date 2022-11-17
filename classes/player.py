from classes.card import Card

class Player:
    def __init__(self, name, balance):
        self.name = name # players name
        self.balance = balance #players balance
        self.hand = []

    def showplayer(self):
        print(f"{self.name} has {self.balance} chips")

    def winstack(self, amount):
        self.balance += amount
        print(f'You won {amount} chips')

    def lossstack(self, amount):
        self.balance -= amount
        print(f'You lost {amount} chips')

    def ante(self, amount):
        self.balance -= amount
        print(f'You bet {amount} chips')

    def showhand(self):
        hand_val = 0
        for x in self.hand:
            Card.card_info(x)
            print(x.point_val)
            hand_val += x.point_val
        print (hand_val)
        return hand_val