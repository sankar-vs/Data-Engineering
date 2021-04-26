'''
@Author: Sankar
@Date: 2021-04-03 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-04 13:38:09
@Title : toBinary
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

def DecimalToBinary(num):
    '''
    Description:
        Covert Decimal to Binary and store them in a list
    Parameter:
        num (int): input from user
    Return:
        list (list): convertion of decimal to binary 
    '''
    list = []
    while(num > 0):
        dig = num % 2
        list.append(dig)
        num = num // 2
    while(len(list)%4 != 0):
        list.append(0)
    list.reverse()
    return list

def print_decimalToBinary():
    '''
    Description:
        Prints the ouput
    Parameter:
        list (list): Output after conversion 
    Return:
        None
    '''
    list = DecimalToBinary(num_regex())
    for i in list:
        print(i, end="")

print_decimalToBinary()