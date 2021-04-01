'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 20:59:49
@Title : Quadratic Equation
'''
from cmath import sqrt
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
    delta = pow(b,2) - (4*a*c)          
    root1 = (-b + sqrt(delta))/(2*a)    
    root2 = (-b - sqrt(delta))/(2*a)    
    print("The roots are {} and {}".format(root1, root2))

print("The Quadratic Equation a*x*x + b*x + c")
while True:
        try:
            a = int(input("Enter 'a': "))
            b = int(input("Enter 'b': "))
            c = int(input("Enter 'c': "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

calucalte_roots(a,b,c)