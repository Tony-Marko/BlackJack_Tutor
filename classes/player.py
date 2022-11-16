class Player:
    def __init__(self, name, balance):
        self.name = name # players name
        self.balance = balance #players balance
        self.playerscards = []

    def showplayer(self):
        print(f"{self.name} has {self.balance} chips")

    def addstack(self, amount):
        self.balance += amount
        print(f'You won {amount} chips')

    def substack(self, amount):
        self.balance -= amount
        print(f'You lost {amount} chips')
