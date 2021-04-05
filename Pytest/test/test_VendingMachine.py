'''
@Author: Sankar
@Date: 2021-04-05 09:25:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-05 09:45:09
@Title : Test of Vending Machine Program
'''
import sys
sys.path.append("..")
import unittest
from src import VendingMachine

class TestVendingMachine(unittest.TestCase):

    def test_calculate_num_of_notes(self):
        """
        Description:
            This method defines test case for VendingMachine.py file
        Parameter:
            None
        Return:
            None
        """
        amount = 5555
        self.assertEqual(VendingMachine.calculate_num_of_notes(amount), [5,1,0,1,0,1,0,0])
        

if __name__ == '__main__':
    unittest.main()