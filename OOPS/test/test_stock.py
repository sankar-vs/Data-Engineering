'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 10:45:09
@Title : Stock Account Management Test
'''
import pytest, os
from src.Stock import Portfolio, Stocks

def test_add_stock():
    port = Portfolio()
    stock = Stocks("NIFTY", 75, 283)
    port.add_stock(stock)
    entries = port.get_entries()
    assert entries["NIFTY"] == stock

def test_print_to_file_stock():
    port = Portfolio()
    stock = Stocks("NIFTY", 75, 283)
    port.add_stock(stock)
    port.print_file()
    

def test_read_from_file_stock():
    port = Portfolio()
    port.read_file()
    entries = port.get_entries()
    assert len(entries) == 1