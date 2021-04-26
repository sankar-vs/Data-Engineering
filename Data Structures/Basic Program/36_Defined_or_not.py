'''
@Author: Sankar
@Date: 2021-04-08 14:31:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 14:32:09
@Title : Basic_Python-36
'''
'''
Write a Python program to determine if variable is defined or not.
'''
try:
    variable
except NameError:
    print("Variable was not defined!")
else:
    print("Variable was defined!")

try:
    variable = 10
except NameError:
    print("Variable was not defined!")
else:
    print("Variable was defined!")