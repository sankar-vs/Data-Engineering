'''
@Author: Sankar
@Date: 2021-04-03 08:42:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 09:12:09
@Title : Temperature Conversion
'''
import pytest
import logging
import re
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
def num_regex_choice():
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        None
    Return:
        num (int): input from user
    '''
    while True:
        try:
            num = input("Enter Choice: ")
            pattern = "^([12])$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        logging.warning("Please choose from 1 or 2")

def get_celsius():
    '''
    Description:
        Get input from user, check whether the input is between -273.15 and 1000, if True then return
    Parameter:
        None
    Return:
        t (float): input from user
    '''
    while True:
        try:
            t = float(input("Enter Celsius: "))
            if (t >= -273.15 and t <= 1000):
                return float(t)
        except:
            pass
        logging.warning("Please enter from -273.15°C to 1000°C")

def get_fahrenheit():
    '''
    Description:
        Get input from user, check whether the input is between 32 and 212, if True then return
    Parameter:
        None
    Return:
        t (float): input from user
    '''
    while True:
        try:
            t = float(input("Enter Fehrenheit: "))
            if (t >= 32 and t <= 212):
                return float(t)
        except:
            pass
        logging.warning("Please enter from 32°F to 212°F")

def convert_to_celsius(t):
    '''
    Description:
        Calculates celsius from fahrenheit from the formula
        (°F − 32) x 5/9 = °C
    Parameter:
        t (float): input from user
    Return:
        celsius (float): coversion from fahrenheit to celsius
    '''
    try:
        celsius = ((t - 32) * (5/9))
        return celsius
    except:
        pass
    logging.error("Check the formula for fahrenheit to celsius conversion")

def convert_to_fahrenheit(t):
    '''
    Description:
        Calculates fahrenheit from celsius from the formula
        (°C × 9/5) + 32 = °F
    Parameter:
        t (float): input from user
    Return:
        celsius (float): coversion from fahrenheit to celsius
    '''
    try:
        fahrenheit = ((t * (9/5)) + 32)
        return fahrenheit
    except:
        pass
    logging.error("Check the formula for celsius to fahrenheit conversion")

def conversion():
    '''
    Description:
        Ask user to select a choice then do the conversion accordingly
        and print the output
    Parameter:
        None
    Return:
        None
    '''
    try:
        print("1. Convert Fahrenheit to Celsius \n2. Convert Celsius to Fahrenheit")
        choice = num_regex_choice()
        if (choice == 1):
            num = get_fahrenheit()
            print("Celsius: {}°C".format(convert_to_celsius(num)))
        else:
            num = get_celsius()
            print("Fahrenheit: {}°F".format(convert_to_fahrenheit(num)))
    except:
        logging.exception("Program has stopped working")

conversion()