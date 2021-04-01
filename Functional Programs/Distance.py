'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 20:45:37
@Title : Euclidean Distance
'''
def calculateEuclideanDsitance():
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
    while True:
        try:
            x = int(input("Enter x co-ordinate: "))
            y = int(input("Enter y co-ordinate: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    distance = pow(x,x)+pow(y,y)
    print("Euclidean distance from the point ({}, {}) to the origin (0, 0) is: {}".format(x, y, distance))

calculateEuclideanDsitance()