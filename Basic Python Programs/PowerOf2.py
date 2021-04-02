'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 10:39:09
@Title : PowerOf2
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
            pattern = "^([1-9]|[12][0-9]|30)$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numerics allowed 1-31")  

def tables_of2(num):
    '''
    Description:
        Prints a table of the powers of 2 that are less than or equal to 2^N.
    Parameter:
        num (int)): input from the user
    Return:
        None
    ''' 
    try:
        for count in range(1, pow(2, num)+1,1):
            table = count * 2
            if( table > pow(2, num)):
                break
            else:
                print("2 * {} = {}".format(count, table))
    except:
        print("Check the input")

tables_of2(num_regex())