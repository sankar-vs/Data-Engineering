'''
@Author: Sankar
@Date: 2021-04-06 21:10:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 21:15:09
@Title :Test Inventory Management
'''
import pytest
from src.InventoryManagement import Management

def test_read_file():
    '''
    Description:
        Reads a file and checks whether the entries dictionary is populated
    Parameter:
        None
    Return:
        None
    '''
    management = Management()
    entries = management.get_entries()
    for i in entries:
        list = entries[i]
        assert len(list) == 2

def test_add_record():
    '''
    Description:
        Adds a record and checks whether the same is reflected in the dictionary
    Parameter:
        None
    Return:
        None
    '''
    management = Management()
    management.add_pulses("Gram", 15, 1500)
    entries = management.get_entries()
    for i in entries:
        list = entries[i]
        assert len(list) == 3