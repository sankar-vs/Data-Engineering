'''
@Author: Sankar
@Date: 2021-04-03 09:16:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 09:42:09
@Title : Day of Week
'''
import pytest
import logging
import re
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
def num_regex_principal():
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        None
    Return:
        amt (int): input from user
    '''
    while True:
        try:
            amt = input("Principal Amount: ")
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, amt)
            if (result):
                return int(amt)
        except:
            pass
        logging.warning("Enter numerics only")

def num_regex_percentage():
    '''
    Description:
        Get input from user, check whether the input is between 1 and 100,
        if True then return
    Parameter:
        None
    Return:
        r (float): input from user
    '''
    while True:
        try:
            r = float(input("Percentage: "))
            if (r >= -273.15 and r <= 1000):
                return float(r)
        except:
            pass
        logging.warning("Percentage from 1 to 100")

def num_regex_year():
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        None
    Return:
        numOfYears (int): input from user
    '''
    while True:
        try:
            numOfYears = input("Enter number of years: ")
            pattern = "^([1-9]|[1-9][0-9]|100)$"
            result = re.match(pattern, numOfYears)
            if (result):
                return int(numOfYears)
        except:
            pass
        logging.warning("Enter between 1 to 100")

def get_input():
    '''
    Description:
        The input from user Principal amount, Rate of Interest and Number of Years, is appended to a list 
    Parameter:
        None
    Return:
        list (list): input from user
    '''
    list = []
    list.append(num_regex_principal())
    list.append(num_regex_percentage())
    list.append(num_regex_year())
    return list

def calculate_monthly_payments(list):
    '''
    Description:
        The Monthly Payment is calculated by the given formula:
        payment = P*r / (1 - (1 + r)^(-n))
        where,
        n = 12*Y, r = R/(1200)
    Parameter:
        list (list): input from user
    Return:
        payment (float): Calculated Monthly Payment
    '''
    try:
        P = list[0]
        r = list[1]/1200
        n = 12 * list[2]
        payment = (P * r) / (1 - pow((1 + r), (-n)))
        return payment
    except:
        raise Exception("Check the inputs")
    logging.error("Check the formulas for Calculating the monthly payments")

print("The Monthly Payment: {}".format(calculate_monthly_payments(get_input())))