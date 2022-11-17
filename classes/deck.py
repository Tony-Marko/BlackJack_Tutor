from . import card
import random

class Deck:
    def __init__( self, num_of_decks):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.num_of_decks = num_of_decks #specify number of decks
        self.total = num_of_decks*52
        self.counter = self.total=1
        self.cards = []

        for x in range(num_of_decks):
            for s in suits:
                for i in range(1,14):
                    str_val = ""
                    if i == 1:
                        str_val = "Ace"
                        pnt_val = 11
                    elif i == 11:
                        str_val = "Jack"
                        pnt_val = 10
                    elif i == 12:
                        str_val = "Queen"
                        pnt_val = 10
                    elif i == 13:
                        str_val = "King"
                        pnt_val = 10
                    else:
                        str_val = str(i)
                        pnt_val = i
                    self.cards.append( card.Card( s , pnt_val , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
        print (f'Cards in Deck: {len(self.cards)}')

    def shuffle_cards(self):
        random.shuffle(self.cards) #shuffle randomizes and replaces the list, no need for useing return
        

    def deal_cards(self, table):
        for x in range(2):
            for player in table:
                player.hand.append(self.cards[self.counter])
                # print(Card.card_info((bicycle.cards[deckcount])))
                self.counter -= 1
        
    def hit(self, player):
        player.hand.append(self.cards[self.counter])
        hand_val = player.showhand()
        self.counter -= 1
        return hand_val
