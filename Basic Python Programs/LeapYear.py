'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 00:45:09
@Title : HarmonicNumber
'''
def test_four_digit_number(x):
    '''
    Description:
        Check if the given number is a four digit number
    Parameter:
        x (str): Input from User
    Return:
        x (int)): returns if length = 4 and if value is greater than 0
    '''        
    if (len(x) == 4 and int(x) > 0): 
        return int(x)  
    else:
        print("Enter a 4 digit number")

def get_input():
    '''
    Description:
        Get input from the User
    Parameter:
        None
    Return:
        year (int)): returns input from the user
    '''   
    while True:
        try:
            year = test_four_digit_number(input("Enter year: "))
            return year
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

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

leap_year(get_input())