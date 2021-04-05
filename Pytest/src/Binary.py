'''
@Author: Sankar
@Date: 2021-04-03 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-04 13:38:09
@Title : Binary to Decimal
'''
import pytest
import logging
import re
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
def num_regex():
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
            num = input("Enter number: ")
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        logging.warning("Enter numerics only greater than 0") 

def shift(list, n):
    '''
    Description:
        Rotates a lost for n number of elements
    Parameter:
        list (list): Binary list
        n (int): number of shifts
    Return:
        list (list): Binary shifted list
    '''
    try:
        n = n % len(list)
        return list[n:] + list[:n]
    except:
        raise Exception
    logging.error("Check inputs")

def toBinary(num):
    '''
    Description:
        Covert Decimal to Binary and store them in a list
    Parameter:
        num (int): input from user
    Return:
        list (list): convertion of decimal to binary 
    '''
    try:
        list = []
        while(num > 0):
            digit = num % 2
            list.append(digit)
            num = num // 2
        while(len(list)%4 != 0):
            list.append(0)
        list.reverse()
        return list
    except:
        raise Exception
    logging.error("Check input")

def toDecimal(list):
    '''
    Description:
        Covert Binary to Decimal
    Parameter:
        list (list): Binary list
    Return:
        value (int): Decimal Value
    '''
    try:
        shifts = len(list) // 2
        shifted_list = shift(list, shifts)
        value = 0
        for i in range(len(shifted_list)):
	        digit = shifted_list.pop()
	        if digit == 1:
		        value = value + pow(2, i)
        print("The decimal value of the number is", value)
        return value
    except:
        raise Exception

toDecimal(toBinary(num_regex()))