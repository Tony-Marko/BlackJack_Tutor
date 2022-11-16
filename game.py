from classes.card import Card
from classes.dealer import Dealer
from classes.deck import Deck
from classes.player import Player

#How many decks to use:
num_of_decks = 3
bicycle = Deck(num_of_decks) #Full deck created
bicycle.shuffle_cards() #Deck shuffled
# bicycle.show_cards()

The_Dealer = Dealer() #Dealer Instance created

Player1 = Player("Tony", 100) #Player instance created
# print(Player1)

Player.showplayer(Player1)

# bicycle.cards(bicycle.total)
print(bicycle.total)
deckcount = bicycle.total-1

# print(bicycle.cards[deckcount])
# Card.card_info((bicycle.cards[deckcount]))

table = [The_Dealer, Player1]

def deal_cards(deckcount):
    for x in range(2):
        for spot in table:
            spot.hand.append(bicycle.cards[deckcount])
            # print(Card.card_info((bicycle.cards[deckcount])))
            deckcount -= 1

deal_cards(deckcount)

Player1.showhand()
The_Dealer.showfirsthand()

def hit(deckcount):
    Player1.hand.append(bicycle.cards[deckcount])
    Player1.showhand()
    deckcount -= 1

def Dealeraction():
    print(f"Dealer's turn: Type hit or stand")
    move = input("What is your move:")
    print(move)
    if move == "hit":
        hit(deckcount)
        Dealeraction()
    if move == "stand":
        print('The dealer stands')
    else:
        print("Invalid response. Try again")
        Dealeraction()

def Playeraction():
    print(f"{Player1.name}'s turn: Type hit or stand")
    move = input("What is your move:")
    print(move)
    if move == "hit":
        hit(deckcount)
        Playeraction()
    if move == "stand":
        Dealeraction()
    else:
        print("Invalid response. Try again")
        Playeraction()

Playeraction()

