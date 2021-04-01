'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 19:16:38
@Title : CoupanNumbers
'''
import random
def test_not_zero(x):
    '''
    Description:
        Check if the given number is greater than 0
    Parameter:
        x (int)): A integer
    Return:
        x (int)): return if value is greater than 0
    '''    
    if int(x) > 0: 
        return int(x)  
    else:
        print("Enter number greater that zero")

# To generate random numbers
def distinct_Coupan_Generator(num):
    '''
    Description:
        Generate random number and to process distinct coupons
    Parameter:
        num (int)): A integer
    Return:
        None
    ''' 
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

# Get input from user until a integer is recieved
while True:
    try:
        numOfCoupans = test_not_zero(input("Enter number of Distinct Coupans: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

distinct_Coupan_Generator(numOfCoupans)