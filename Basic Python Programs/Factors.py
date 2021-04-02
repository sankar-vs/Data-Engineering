'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 10:54:09
@Title : PrimeFactorization Method
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
            pattern = "^([2-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numerics greater than 1")

def prime_factors(num):
    '''
    Description:
        Find the Prime Factors of the given number and prints them
    Parameter:
        num (int): A Positive Integer
    Return:
        None
    ''' 
    try:
        prime = []
        while num % 2 == 0:
            prime.append(2)
            num = int (num / 2)
        for count in range(3, num+1, 2):
            while num % count == 0:
                prime.append(count)
                num = int(num / count)
        if num > 2:
            prime.append
        print("Prime Factors are: {}".format(prime))    
    except TypeError:
        print("Check the input")

prime_factors(num_regex())