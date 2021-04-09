'''
@Author: Sankar
@Date: 2021-04-09 10:13:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 10:20:09
@Title : Dictionary_Python-11
'''
'''
Write a Python program to convert a list into a nested dictionary of keys.
'''
list = [1,2,3]
updatedDict = dict = {}
for i in list:
    dict[i] = {}
    dict = dict[i]
print(updatedDict)