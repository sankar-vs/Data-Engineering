'''
@Author: Sankar
@Date: 2021-04-04 18:40:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-05 08:58:09
@Title : Test case for Binary program
'''
import sys
sys.path.append("..")
import unittest
from src import Binary

class TestBinary(unittest.TestCase):

    def test_to_decimal(self):
        """
        Description:
            This method defines test case for Binary.py file
        Parameter:
            None
        Return:
            None
        """
        decimal = 100
        self.assertEqual(Binary.toBinary(decimal), [0,1,1,0,0,1,0,0])
        shifted_list = [0,1,0,0,0,1,1,0]
        self.assertEqual(Binary.shift([0,1,1,0,0,1,0,0], 4), shifted_list)
        value = 70
        self.assertEqual(Binary.toDecimal([0,1,1,0,0,1,0,0]), value)
        

if __name__ == '__main__':
    unittest.main()