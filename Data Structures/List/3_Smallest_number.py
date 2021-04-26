'''
@Author: Sankar
@Date: 2021-04-09 12:07:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 12:13:09
@Title : List_Python-3
'''
'''
Write a Python program to get the smallest number from a list.
'''

list = [1,2,3,4,6,10,0]
minimum = list[0]
for i in list:
    if (minimum>i):
        minimum = i
print("Minimum of list {} is: {}".format(list, minimum))
print("Minimum of list using function {} is: {}".format(list, min(list)))