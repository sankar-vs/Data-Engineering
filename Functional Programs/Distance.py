'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 12:25:37
@Title : Euclidean Distance
'''
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
            pattern = "^([+-]?[0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numeric integer")

def calculateEuclideanDistance():
    '''
    Description:
        Getting the x and y co-ordinates from the user and
        Calculate the Euclidean Distance by the given formula x**x+y**y
        and print the distance
    Parameter:
        None
    Return:
        None
    '''
    try:
        x = num_regex_int("Enter x co-ordinate: ")
        y = num_regex_int("Enter y co-ordinate: ")
        distance = pow(abs(x),abs(x))+pow(abs(y),abs(y))
        print("Euclidean distance from the point ({}, {}) to the origin (0, 0) is: {}".format(x, y, distance))
    except:
        pass

calculateEuclideanDistance()