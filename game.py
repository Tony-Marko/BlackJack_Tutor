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
The_Dealer.showfirsthand() #same as showhand but only shows the second card

Player.action(Player1, bicycle)
Dealer.action(The_Dealer, bicycle)

print (f"The Dealer has {The_Dealer.hand_val}")
print(f"{Player1.name} has {Player1.hand_val}")
if The_Dealer.hand_val > 21:
    print (f"{Player1.name} wins!")
elif Player1.hand_val > 21:
    print (f"The Dealer wins!")
else:
    if The_Dealer.hand_val == Player1.hand_val:
        print ("Push!")
    elif The_Dealer.hand_val < Player1.hand_val:
        print (f"{Player1.name} wins!")
    elif The_Dealer.hand_val > Player1.hand_val:
        print ("Dealer wins!")





