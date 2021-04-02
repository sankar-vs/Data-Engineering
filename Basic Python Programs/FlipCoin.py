'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 00:08:09
@Title : FlipCoin
'''
import random
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
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numerics greater than 0")

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
        print("Percentage of Heads: {}% \nPercentage of Tails: {}%".format((countHeads/numberOfFlips)*100, (countTails/numberOfFlips)*100))
    except:
        print("Check input")
        
calculate_perc_of_heads_and_tails(num_regex())