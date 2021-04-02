'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 00:18:09
@Title : HarmonicNumber
'''
import re
def num_regex():
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then print return
    Parameter:
        None
    Return:
        num (int): input from user
    '''
    while True:
        try:
            num = input("Enter a number: ")
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numerics greater than 0")  

def calculate_harmonic(num):
    '''
    Description:
        Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
    Parameter:
        num (int): Input from User
    Return:
        None
    '''
    try:
        harmonic = 0
        for count in range(1, num+1, 1):
            div = (1/count)
            harmonic += div
        print("The {}th Harmonic number: {}".format(num, harmonic))
    except:
        print("Check input")    

calculate_harmonic(num_regex())