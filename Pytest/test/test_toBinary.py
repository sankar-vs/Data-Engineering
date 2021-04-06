'''
@Author: Sankar
@Date: 2021-04-05 09:25:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-05 09:45:09
@Title : Test of toBinary Program
'''
import sys
sys.path.append("..")
import unittest
from src import toBinary

class TestBinary(unittest.TestCase):

    def test_decimal_to_binary(self):
        """
        Description:
            This method defines test case for toBinary.py file
        Parameter:
            None
        Return:
            None
        """
        decimal = 106
        self.assertEqual(toBinary.DecimalToBinary(decimal), [0,1,1,0,1,0,1,0])
        
    def test_decimal_to_binary_negative(self):
        """
        Description:
            This method defines negative test case for toBinary.py file
        Parameter:
            None
        Return:
            None
        """
        decimal = 100
        self.assertNotEqual(toBinary.DecimalToBinary(decimal), [0,1,1,0,1,0,1,0])
        self.assertRaises(Exception, toBinary.DecimalToBinary, "100")

if __name__ == '__main__':
    unittest.main()