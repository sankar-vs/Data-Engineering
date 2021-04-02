'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 19:16:38
@Title : CoupanNumbers
'''
import random
import re
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
            num = input("Enter number of Distinct Coupans: ")
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numerics greater than 0") 

def distinct_coupan_generator(num):
    '''
    Description:
        Generate random number and to process distinct coupons
    Parameter:
        num (int)): input from user
    Return:
        None
    ''' 
    try:
        array = []
        count = i = 0
        while (i < (num+count)):
            rand = random.randint(1, num)
            i += 1
            if (len(array) == 0):
                array.append(rand)
            else:
                exists = rand in array
                if (exists):
                    count += 1
                    continue
                else:
                    array.append(rand)
        print(array)   
    except:
        print("Check Input")         

distinct_coupan_generator(num_regex())