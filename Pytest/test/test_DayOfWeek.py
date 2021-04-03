'''
@Author: Sankar
@Date: 2021-04-03 08:32:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 11:59:09
@Title : Test case for Day of Week program
'''
import pytest
from src import DayOfWeek

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

def test_regex_day():
    '''
    Description:
        Test of the function num_regex_day() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert DayOfWeek.num_regex_day("3") == 3

def test_regex_month():
    '''
    Description:
        Test of the function num_regex_month() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert DayOfWeek.num_regex_month("12") == 4

def test_regex_year():
    '''
    Description:
        Test of the function num_regex_year() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert DayOfWeek.num_regex_year("2021") == 2021

def test_gregorian_calender():
    '''
    Description:
        Test of the function gregorian_calender() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert DayOfWeek.gregorian_calender(input()) == "Saturday"