from classes.card import Card
from classes.deck import Deck

class Player:
    def __init__(self, name, balance):
        self.name = name # players name
        self.balance = balance #players balance
        self.hand = []
        self.status = ""
        self.hand_val = 0

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
        for x in self.hand:
            Card.card_info(x)
            if x.string_val == "Ace":
                has_Ace = True
                print(has_Ace)
            self.hand_val += x.point_val
        print (f"Your hand: {self.hand_val}")
        if len(self.hand) == 2 and self.hand_val == 21:
            print("BLACKJACK!")
            self.status = "BLACKJACK"
        return self.hand_val

    def action(self, bicycle):
        if self.status == "BLACKJACK":
            print (f"{self.name} wins!")
            return
        print(f"{self.name}'s turn: Type hit or stand")
        move = input("What is your move:")
        print(move)
        if move == "hit":
            self.hand_val = Deck.hit(bicycle, self)
            if self.hand_val > 21:
                print (f"You have {self.hand_val} BUST!")
                return self.hand_val
            if self.hand_val == 21:
                print(f"{self.name} stands with {self.hand_val}")
                return self.hand_val
            else: 
                Player.action(self, bicycle)
        elif move == "stand":
            print(f"{self.name} stands")
            return self.hand_val   
        else:
            print("Invalid response. Try again")
            Player.action(self, bicycle)



