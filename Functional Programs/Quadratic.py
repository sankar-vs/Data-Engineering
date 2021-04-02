'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 12:35:49
@Title : Quadratic Equation
'''
from cmath import sqrt
import re
def num_regex_int(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        x (str) : Statement to be printed to take the the inputs from user
    Return:
        num (int): input from user
    '''
    while True:
        try:
            num = input(x)
            pattern = "^([+-]?[0-9]{,9})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numeric integer")

def calucalte_roots(a, b, c):
    '''
    Description:
        Calculate the roots for Quadratic Equation by the given formula 
        delta = b*2 - 4*a*c
        Root 1 of x = (-b + sqrt(delta))/(2*a)
        Root 2 of x = (-b - sqrt(delta))/(2*a)
    Parameter:
        None
    Return:
        None
    '''
    try:
        delta = pow(b,2) - (4*a*c)          
        root1 = (-b + sqrt(delta))/(2*a)    
        root2 = (-b - sqrt(delta))/(2*a)    
        print("The roots are {} and {}".format(root1, root2))
    except:
        pass

print("The Quadratic Equation a*x*x + b*x + c")

a = num_regex_int("Enter 'a': ")
b = num_regex_int("Enter 'b': ")
c = num_regex_int("Enter 'c': ")
calucalte_roots(a,b,c)