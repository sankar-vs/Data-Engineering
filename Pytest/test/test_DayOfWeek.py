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

    def test_gregorian_calender_negative(self):
        """
        Description:
            This method define for negative test case for DayOfWeek.py file
        Parameter:
            None
        Return:
            None
        """
        list = [3, 5, 2021]
        result = DayOfWeek.gregorian_calender(list)
        self.assertNotEqual(result, "Saturday")

        list = ["3", 5, 2021]
        self.assertRaises((TypeError, ValueError), DayOfWeek.gregorian_calender, list)

if __name__ == '__main__':
    unittest.main()
