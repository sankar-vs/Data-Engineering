'''
@Author: Sankar
@Date: 2021-04-03 11:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 11:54:09
@Title : Test of MonthlyPayment Program
'''
import pytest
from src import MonthlyPayment

@pytest.fixture
def input_total():
    '''
    Description:
        Set the fixture of inputs to be goven for he test case
    Parameter:
        None
    Return:
        list (list): integer elements
    '''
    list = [120000, 12, 1]
    return list

def test_monthly_payment():
    '''
    Description:
        test of the function calculate_monthly_payments() to check the 
        ouput is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert MonthlyPayment.calculate_monthly_payments(input()) == 10661.854641400992