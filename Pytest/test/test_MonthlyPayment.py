'''
@Author: Sankar
@Date: 2021-04-03 11:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-05 09:15:09
@Title : Test of MonthlyPayment Program
'''
import sys
sys.path.append("..")
import unittest
from src import MonthyPayment

class TestMonthlyPayment(unittest.TestCase):

    def test_calculate_monthly_payment(self):
        """
        Description:
            This method defines test case for MonthlyPayment.py file
        Parameter:
            None
        Return:
            None
        """
        list = [100000, 10.00, 1]
        self.assertEqual(MonthyPayment.calculate_monthly_payments(list), 8791.588723000987)
        

if __name__ == '__main__':
    unittest.main()