'''
@Author: Sankar
@Date: 2021-04-10 08:30:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-10 08:35:09
@Title : List_Python-15
'''
'''
Write a Python program to find common items from two lists.
'''
list1 = [1, 2, 3, 5]
list2 = [2, 4, 5, 7]

common = [i for i in list1 if i in list2]

print(common)