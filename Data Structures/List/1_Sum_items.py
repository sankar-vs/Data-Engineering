'''
@Author: Sankar
@Date: 2021-04-09 11:59:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 12:05:09
@Title : List_Python-1
'''
'''
Write a Python program to sum all the items in a list.
'''
list = [1,2,3,4,6,7,8,9,10]
sum = 0
for i in list:
    sum += i
print("Sum of list {} is: {}".format(list, sum))