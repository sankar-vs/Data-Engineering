'''
@Author: Sankar
@Date: 2021-04-03 08:32:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 11:59:09
@Title : Test case for Day of Week program
'''
import os
import pytest
#os.chdir("../")
from src import DayOfWeek as week

@pytest.fixture
def input():
    '''
    Description:
        Set the fixture of inputs to be given for the test case
    Parameter:
        None
    Return:
        list (list): integer elements
    '''
    list = [3, 4, 2021]
    return list

def test_gregorian_calender(input):
    '''
    Description:
        Test of the function gregorian_calender() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert week.gregorian_calender(input) == "Saturday"