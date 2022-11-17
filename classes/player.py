from classes.card import Card
from classes.deck import Deck

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
            # print(x.point_val)
            hand_val += x.point_val
        print (f"Your hand: {hand_val}")
        if len(self.hand) == 2 and hand_val == 21:
            print("BLACKJACK!")
        return hand_val

    def action(self, bicycle):
        print(f"{self.name}'s turn: Type hit or stand")
        move = input("What is your move:")
        print(move)
        if move == "hit":
            hand_val = Deck.hit(bicycle, self)
            if hand_val > 21:
                print ("BUST!")
                return
            else: 
                Player.action(self, bicycle)
        elif move == "stand":
            print("Player stands")
            return
        else:
            print("Invalid response. Try again")
            Player.action(self, bicycle)



