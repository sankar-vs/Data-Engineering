'''
@Author: Sankar
@Date: 2021-04-03 12:02:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 12:54:09
@Title : Test of SQRT Program
'''
import pytest
from src import SQRT

@pytest.fixture
def input_total():
    '''
    Description:
        Set the fixture of inputs to be goven for he test case
    Parameter:
        None
    Return:
        num (int): integer input
    '''
    num = 25
    return num

def test_regex_num():
    '''
    Description:
        Test of the function num_regex_year() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert SQRT.num_regex("25") == 25

def test_calculate_sqrt():
    '''
    Description:
        Test of the function calculate_sqrt() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert SQRT.calculate_sqrt(input()) == 5.0