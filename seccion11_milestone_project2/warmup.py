#python  seccion11_milestone_project2/warmup.py
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#card class
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self): #funcion de aqui es importante para imprimir el rank con suit parecido a un toString
        return self.rank + ' of ' + self.suit


three_of_clubs = Card("Clubs","Three")
print(three_of_clubs)

two_hearts = Card(suits[0],ranks[0])
print(two_hearts)

print(two_hearts.rank)
print(two_hearts.value)
print(two_hearts.suit)
print(values[two_hearts.rank])


#deck class
class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


mydeck = Deck()
print(len(mydeck.all_cards))
print(mydeck.all_cards[0])
mydeck.shuffle()
print(mydeck.all_cards[0])
my_card = mydeck.deal_one()
print(my_card)

#player class

class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

jose = Player("Jose")
print(jose)
jose.add_cards(two_hearts)
print(jose)
jose.add_cards([two_hearts,two_hearts,two_hearts])
print(jose)
jose.remove_one()
print(jose)





