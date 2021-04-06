'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 12:50:09
@Title : Deck of Cards
'''
import random

class Card:
    '''
    Class:
        Card

    Description:
        Creates a card

    Functions:
        show() -> str

    Variable:
        None
    '''
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        '''
        Description:
            Shows the value of a single card
        Parameter:
            None
        Return:
            None
        '''
        if self.value == 1:
            trueValue = "Ace"
        elif self.value == 11:
            trueValue = "Jack"
        elif self.value == 12:
            trueValue = "Queen"
        elif self.value == 13:
            trueValue = "King"
        else:
            trueValue = str(self.value)
        print("{} of {}".format(trueValue, self.suit))

class Deck:
    '''
    Class:
        Deck

    Description:
        Creates a Deck of Cards in a list (52 Cards in a single deck)

    Functions:
        build() 
        show()
        shuffle()
        drawCard()

    Variable:
        None
    '''
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        '''
        Description:
            Creates a deck of 52 cards
        Parameter:
            None
        Return:
            None
        '''
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        '''
        Description:
            Shows the created deck
        Parameter:
            None
        Return:
            None
        '''
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        '''
        Description:
            Shuffles the deck created deck
        Parameter:
            None
        Return:
            None
        '''
        for i in range(1,14):
            random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()

class Player:
    '''
    Class:
        Player

    Description:
        Creates a Player having a hand of 13 Cards in players deck

    Functions:
        drawHand() 
        showHand()

    Variable:
        None
    '''
    def __init__(self, name):
        self.name = name
        self.hand = []

    def drawHand(self, deck):
        '''
        Description:
            Draws card from the shuffled deck to player's hand (13 cards)
        Parameter:
            None
        Return:
            None
        '''
        for i in range(1, 14):
            self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        '''
        Description:
            Shows the card from player's hand (13 cards)
        Parameter:
            None
        Return:
            None
        '''
        print("Player: {}".format(self.name))
        for card in self.hand:
            card.show()

def distribute_card():
    '''
        Description:
            Disptributes card to 4 players
        Parameter:
            None
        Return:
            None
    '''
    try:
        deck = Deck()
        deck.shuffle()

        sam = Player("Sam")
        sam.drawHand(deck)
        sam.showHand()

        kevin = Player("Kevin")
        kevin.drawHand(deck)
        kevin.showHand()

        diana = Player("Diana")
        diana.drawHand(deck)
        diana.showHand()

        adriana = Player("Adriana")
        adriana.drawHand(deck)
        adriana.showHand()
    except:
        pass

distribute_card()