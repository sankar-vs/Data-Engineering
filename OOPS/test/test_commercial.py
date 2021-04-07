'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 05:37:09
@Title : Test Commercial Data Processing
'''
import pytest, os
from src.Commercial import StockAccount

def test_buy_stock():
    '''
        Description:
            Test to Buy a stock
        Parameter:
            None
        Return:
            None
    '''
    stock = StockAccount("account")
    stock.buy("NIFTY", 10000)
    entries = stock.get_entries()
    assert entries["NIFTY"] == ["NIFTY", 10000]

def test_sell_stock():
    '''
        Description:
            Test to Sell a stock
        Parameter:
            None
        Return:
            None
    '''
    stock = StockAccount("account")
    stock.sell("NIFTY", 15000)
    entries = stock.get_entries()
    assert entries["NIFTY"] == ["NIFTY", -5000]

def test_save_stock():
    '''
        Description:
            Test Save the details to file
        Parameter:
            None
        Return:
            None
    '''
    stock = StockAccount("account")
    stock.save("account")
    if os.path.isfile("OOPS/src/resources/account.csv"):
        with open("OOPS/src/resources/account.csv", "r") as f:
            data = f.readlines()
            assert len(data) == 1