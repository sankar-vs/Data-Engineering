'''
@Author: Sankar
@Date: 2021-04-10 08:52:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-10 08:57:09
@Title : List_Python-17
'''
'''
Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]   
'''
import itertools
list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

list1.sort()
new_list = list(list1 for list1,_ in itertools.groupby(list1))
print(new_list)