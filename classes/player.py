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

    def showhand(self):
        for x in self.hand:
            Card.card_info(x)