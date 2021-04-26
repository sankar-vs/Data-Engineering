'''
@Author: Sankar
@Date: 2021-04-03 07:32:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 08:38:09
@Title : Day of Week
'''
import pytest
import logging
import re
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
def num_regex_day():
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
            num = input("Day: ")
            pattern = "^([1-9]|[12][0-9]|3[01])$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        logging.warning("Days are from 1 to 31")

def num_regex_month():
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
            num = input("Month: ")
            pattern = "^([1-9]|[1][0-2])$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        logging.warning("Months are from 1 to 12")

def num_regex_year():
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
            num = input("Enter year: ")
            pattern = "^([1-9][0-9]{3})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        logging.warning("Enter year of 4 digits")

def get_input():
    '''
    Description:
        The input from user day, month and year, is appended to a list 
    Parameter:
        None
    Return:
        list (list): input from user
    '''
    try:
        list = []
        logging.info("Getting Inputs")
        list.append(num_regex_day())
        list.append(num_regex_month())
        list.append(num_regex_year())
        print(list)
        return list
    except:
        logging.exception("Check the inputs")
    

def gregorian_calender(list):
    '''
    Description:
        The gregorian calender day is calculated by use of formulas:
        y0 = y - (14-m) / 12
        x = y0 + y0/4 - y0/100 + y0/400
        m0 =  m + 12 *((14- m) / 12)- 2
        d0 = (d + x + 30 * m0/12)%7;
    Parameter:
        list (list): input from user
    Return:
        None
    '''
    try:
        day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        d = list[0]
        m = list[1]
        y = list[2]

        y0 = y - ((14-m)//12)
        x = y0 + (y0//4) - (y0//100) + (y0//400)
        m0 =  m + 12 * ((14- m) // 12) - 2
        d0 = (d + x + 30 * m0//12) % 7
        return day[d0]
    except TypeError:
        logging.exception("Check the calculation of day")
        raise TypeError("Check the inputs")
    except ValueError:
        logging.exception("Check the inputs")
        raise ValueError("Check the inputs")
        
    
print("The day is: {}".format(gregorian_calender(get_input())))