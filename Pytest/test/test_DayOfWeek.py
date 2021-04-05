'''
@Author: Sankar
@Date: 2021-04-03 08:32:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-05 08:40:09
@Title : Test case for Day of Week program
'''
import sys
sys.path.append("..")
import unittest
from src import DayOfWeek

class TestDayOfWeek(unittest.TestCase):

    def test_gregorian_calender(self):
        """
        Description:
            This method define for test case for DayOfWeek.py file
        Parameter:
            None
        Return:
            None
        """
        list = [3, 4, 2021]
        result = DayOfWeek.gregorian_calender(list)
        self.assertEqual(result, "Saturday")

if __name__ == '__main__':
    unittest.main()

# @pytest.fixture
# def input():
#     '''
#     Description:
#         Set the fixture of inputs to be given for the test case
#     Parameter:
#         None
#     Return:
#         list (list): integer elements
#     '''
#     list = [3, 4, 2021]
#     return list

# def test_gregorian_calender(input):
#     '''
#     Description:
#         Test of the function gregorian_calender() to check the 
#         output is equal to that of the expected result
#     Parameter:
#         None
#     Return:
#         None
#     '''
#     assert gregorian_calender(input) == "Sunday"