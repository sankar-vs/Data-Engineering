'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 11:34:09
@Title : HarmonicNumber
'''
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
            num = input("Enter year: ")
            pattern = "^([1-9][0-9]{3})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Enter year of 4 digits")

def leap_year(year):
    '''
    Description:
        Determine if it is a Leap Year and prints the result
    Parameter:
        None
    Return:
        None
    '''
    try:
        if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
            print("{} is Leap Year".format(year))
        else:
            print("{} is Not a Leap Year".format(year))
    except TypeError:
        print("Check input")

leap_year(num_regex())