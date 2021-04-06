'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 16:10:09
@Title : Test Deck of Cards
'''
import pytest
from cards import Card, Deck, Player

def test_card(capsys):
    '''
        Description:
            Test Creation of a Card
        Parameter:
            None
        Return:
            None
    '''
    card = Card("Spades", 1)
    card.show()
    out, err = capsys.readouterr()
    assert out == "Ace of Spades\n"
    assert err == ""

def test_card_negative(capsys):
    '''
        Description:
            Checks the creation of card for a wrong ouput
        Parameter:
            None
        Return:
            None
    '''
    card = Card("Spades", 1)
    card.show()
    out, err = capsys.readouterr()
    assert out != "King of Spades\n"
    assert err == ""

def test_deck_draw(capsys):
    '''
        Description:
            Test for checking the Pop of the last card in the deck
        Parameter:
            None
        Return:
            None
    '''
    deck = Deck()
    card = deck.drawCard()
    card.show()
    out, err = capsys.readouterr()
    assert out == "King of Hearts\n"
    assert err == ""

def test_deck_draw_negative(capsys):
    '''
        Description:
            Test for checking the Pop of the last card in the deck for a wrong output
        Parameter:
            None
        Return:
            None
    '''
    deck = Deck()
    card = deck.drawCard()
    card.show()
    out, err = capsys.readouterr()
    assert out != "Ace of Hearts\n"
    assert err == ""