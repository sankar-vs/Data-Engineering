'''
@Author: Sankar
@Date: 2021-04-03 17:27:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-04 18:15:09
@Title : Vending Machine
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
        amt (int): input from user
    '''
    while True:
        try:
            amt = input("Enter amount: ")
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, amt)
            if (result):
                return int(amt)
        except ValueError:
            pass
        logging.warning("Enter numerics only greater than 0") 

def calculate_num_of_notes(amount):
    '''
    Description:
        Calculate number of notes to withdrwn from the vending machine
    Parameter:
        amount (int): amount from user
    Return:
        result (list): number of notes to be withdrawn
    '''
    try:
        vending = [1000,500,100,50,10,5,2,1]
        result = [0 for i in range(len(vending))]
        for i in (range(len(vending))):
            if(amount //vending[i] > 0):
                result[i] = (amount//vending[i])
                amount = int(amount % vending[i])

        for i in (range(len(vending))):
            if(result[i] > 0):
                print("{} * {} = {}".format(vending[i],result[i],(vending[i]*result[i])))
        
        return result
    except (ValueError, TypeError):
        raise Exception("Check Inputs")
    logging.error("Check input")    

calculate_num_of_notes(num_regex())