'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 12:50:09
@Title : Test Commercial Data Processing
'''
import pytest, os
from commercial import StockAccount

def test_buy_stock():
    stock = StockAccount("account")
    stock.buy("NIFTY", 10000)
    entries = stock.get_entries()
    assert entries["NIFTY"] == ["NIFTY", 10000]

def test_sell_stock():
    stock = StockAccount("account")
    stock.sell("NIFTY", 15000)
    entries = stock.get_entries()
    assert entries["NIFTY"] == ["NIFTY", -5000]

def test_save_stock():
    stock = StockAccount("account")
    stock.save("account")
    if os.path.isfile("account.csv"):
        with open("account.csv", "r") as f:
            data = f.readlines()
            assert len(data) == 1