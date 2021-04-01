'''
@Author: Sankar
@Date: 2021-04-01 09:36:10
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 19:41:20
@Title : Gambler
'''
import random
import sys
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

def gamble():
    '''
    Description:
        Gambles from a stake to reach a goal for a specified number of bets to be made
        The stake, goal and number of bets is taken as input from user
        Finally, prints the number of Wins and Loss,
        Percentage of Wins and Losses for the number of bets were made
    Parameter:
        None
    Return:
        None
    '''
    while True:
        try:
            stake = test_not_zero(input("Enter stake: "))
            goal = test_not_zero(input("Enter goal: "))
            numOfBets = test_not_zero(input("Enter total number of times to bet: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    count = countLoss = countWon = 0
    while (( stake < goal and stake > 0) and (count < numOfBets)): 
        gamble = random.randint(0,1)
        if (gamble == 0) :
            countLoss += 1
            stake -= 1
        else:
            countWon += 1
            stake += 1
        count += 1
    percentageOfWins = (countWon/numOfBets)*100
    percentageOfLoss = (countLoss/numOfBets)*100
    print("Number of Wins: {} and Number of Losses: {}".format(countWon, countLoss))
    print("Percentage of Wins: {}% and Percentage of Loss: {}%".format(percentageOfWins, percentageOfLoss))

gamble()