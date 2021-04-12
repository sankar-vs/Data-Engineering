'''
@Author: Sankar
@Date: 2021-04-07 19:50:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 19:54:09
@Title : Basic_Python-7
'''
'''
Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

list = [1, 5, 8, 3]

check = 3 in list
print("3 -> {}: {}".format(list, check))
check = -1 in list
print("-1 -> {}: {}".format(list, check))