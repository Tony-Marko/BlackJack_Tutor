from classes.dealer import Dealer
from classes.deck import Deck
from classes.player import Player

#How many decks to use:
num_of_decks = 3
bicycle = Deck(num_of_decks) #Full deck created
bicycle.shuffle_cards() #Deck shuffled

The_Dealer = Dealer() #Dealer Instance created

Player1 = Player("Tony", 100) #Player instance created

Player.showplayer(Player1)

table = [Player1, The_Dealer]

Deck.deal_cards(bicycle, table)

Player1.showhand()
The_Dealer.showfirsthand()

Player.action(Player1, bicycle)
Dealer.action(The_Dealer, bicycle)



# def Dealeraction():
#     print(f"Dealer's turn: Type hit or stand")
#     move = input("What is your move:")
#     print(move)
#     if move == "hit":
#         hit(deckcount)
#         Dealeraction()
#     if move == "stand":
#         print('The dealer stands')
#     else:
#         print("Invalid response Dealer. Try again")
#         Dealeraction()

# def Playeraction():
#     print(f"{Player1.name}'s turn: Type hit or stand")
#     move = input("What is your move:")
#     print(move)
#     if move == "hit":
#         hit(deckcount)
#         Playeraction()
#     if move == "stand":
#         Dealeraction()
#     else:
#         print("Invalid response. Try again")
#         Playeraction()



