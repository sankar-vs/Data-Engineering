'''
@Author: Sankar
@Date: 2021-04-03 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-03 09:42:09
@Title : sqrt using Newton's method
'''
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
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

DecimalToBinary(num_regex())