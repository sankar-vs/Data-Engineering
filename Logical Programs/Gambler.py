'''
@Author: Sankar
@Date: 2021-04-01 09:36:10
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 11:49:20
@Title : Gambler
'''
import random
import re
def num_regex(x):
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
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numerics greater than 0")

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
    try:
        stake = num_regex("Enter stake: ")
        check = num_regex("Enter goal: ")
        if (check > stake):
            goal = check
        else:
            goal = stake + 1
        numOfBets = num_regex("Enter total number of times to bet: ")  
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
    except:
        print("Check Input")

gamble()