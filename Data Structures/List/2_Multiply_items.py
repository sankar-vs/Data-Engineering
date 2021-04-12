'''
@Author: Sankar
@Date: 2021-04-09 12:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 12:07:09
@Title : List_Python-2
'''
'''
Write a Python program to multiplies all the items in a list.
'''
list = [1,2,3,4,6,10]
multiplication = 1 
for i in list:
    multiplication *= i
print("Product of list {} is: {}".format(list, multiplication))