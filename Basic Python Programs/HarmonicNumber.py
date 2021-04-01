'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 00:18:09
@Title : HarmonicNumber
'''
def test_positive_integer(x):
    '''
    Description:
        Check if the given number is greater than 0
    Parameter:
        x (str): Input from User
    Return:
        x (int)): returns if value is greater than 0
    '''   
    if int(x) > 0:
        return int(x)  
    else:
        print("Enter number greater that zero")

def get_input():
    '''
    Description:
        Get input from the User
    Parameter:
        None
    Return:
        num (int)): returns input from the user
    '''   
    while True:
        try:
            num = test_positive_integer(input("Enter a number: "))
            return num
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

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
    except TypeError:
        print("Check input")    

calculate_harmonic(get_input())