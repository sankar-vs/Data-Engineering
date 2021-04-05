'''
@Author: Sankar
@Date: 2021-04-03 12:02:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-05 09:18:09
@Title : Test of SQRT Program
'''
import sys
sys.path.append("..")
import unittest
from src import SQRT

class TestSQRT(unittest.TestCase):

    def test_calculate_sqrt(self):
        """
        Description:
            This method defines test case for SQRT.py file
        Parameter:
            None
        Return:
            None
        """
        value = 25
        self.assertEqual(SQRT.calculate_sqrt(value), 5.0)
        

if __name__ == '__main__':
    unittest.main()