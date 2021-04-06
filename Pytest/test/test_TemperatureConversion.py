'''
@Author: Sankar
@Date: 2021-04-03 12:02:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 12:54:09
@Title : Test of SQRT Program
'''
import sys
sys.path.append("..")
import unittest
from src import TemperatureConversion

class TestTemperatureConversion(unittest.TestCase):

    def test_conversion(self):
        """
        Description:
            This method defines test case for TemperatureConversion.py file
        Parameter:
            None
        Return:
            None
        """
        celsius = 10
        fahrenheit = 50
        self.assertEqual(TemperatureConversion.convert_to_fahrenheit(celsius),50.0)
        self.assertEqual(TemperatureConversion.convert_to_celsius(fahrenheit),10.0)

    def test_conversion_negative(self):
        """
        Description:
            This method defines negative test case for TemperatureConversion.py file
        Parameter:
            None
        Return:
            None
        """
        celsius = 20
        fahrenheit = 60
        self.assertNotEqual(TemperatureConversion.convert_to_fahrenheit(celsius),50.0)
        self.assertNotEqual(TemperatureConversion.convert_to_celsius(fahrenheit),10.0)
        self.assertRaises(Exception, TemperatureConversion.convert_to_celsius, "10.0")
        self.assertRaises(Exception, TemperatureConversion.convert_to_fahrenheit, "20.0")

if __name__ == '__main__':
    unittest.main()