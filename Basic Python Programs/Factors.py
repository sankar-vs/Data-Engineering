'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 22:34:09
@Title : PrimeFactorization Method
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

prime_factors(get_input())