'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 00:08:09
@Title : FlipCoin
'''
import random
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

def calculate_perc_of_heads_and_tails(numberOfFlips):
    '''
    Description:
        Flip Coin and print percentage of Head and Tails
        Get number of time to flip a coin from user and use random function to generate 0(Tails),1(Heads)
    Parameter:
        numOfFlips (int): Input from User
    Return:
        None
    ''' 
    try:
        countHeads = countTails = 0
        for flip in range(numberOfFlips):
            if (random.random() > 0.5): 
                countHeads +=  1
            else:
                countTails +=  1
        print("Percentage of Heads: {}% \n Percentage of Tails: {}%".format((countHeads/numberOfFlips)*100, (countTails/numberOfFlips)*100))
    except TypeError:
        print("Check input")
        
calculate_perc_of_heads_and_tails(get_input())