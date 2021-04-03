'''
@Author: Sankar
@Date: 2021-04-03 12:02:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 12:54:09
@Title : Test of SQRT Program
'''
import pytest
from src import TemperatureConversion

@pytest.fixture
def input_total():
    '''
    Description:
        Set the fixture of inputs to be given for the test case
    Parameter:
        None
    Return:
        num (int): integer input
    '''
    num = 50
    return num

def test_convert_celsius():
    '''
    Description:
        Test of the function convert_to_celsius() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert TemperatureConversion.convert_to_celsius(input()) == 10.0

def test_convert_fehrenheit():
    '''
    Description:
        Test of the function convert_to_celsius() to check the 
        output is equal to that of the expected result
    Parameter:
        None
    Return:
        None
    '''
    assert TemperatureConversion.convert_to_fahrenheit(input()) == 122.0