'''
@Author: Sankar
@Date: 2021-04-03 08:32:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 08:33:09
@Title : Day of Week
'''
import pytest
from src import DayOfWeek

@pytest.fixture
def input_total():
    list = [3, 4, 2021]
    return list

def test_gregorian_calender():
    assert DayOfWeek.gregorian_calender(input_total()) == "Saturday"