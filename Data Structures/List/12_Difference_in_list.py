'''
@Author: Sankar
@Date: 2021-04-10 07:22:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-10 07:30:09
@Title : List_Python-12
'''
'''
Write a Python program to get the difference between the two lists.
'''
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
list = [i for i in list1+list2 if i not in list1 or i not in list2]
print("Difference between {} and {}: {}".format(list1, list2, list))