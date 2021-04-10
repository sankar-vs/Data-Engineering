'''
@Author: Sankar
@Date: 2021-04-10 08:27:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-10 08:30:09
@Title : List_Python-14
'''
'''
Write a python program to check whether two lists are circularly identical.
'''
import numpy

list1 = [1, 1, 1, 0, 0]
list2 = [1, 1, 0, 0, 1]

def is_dep(list1,list2):
    for i in range(len(list1)):
        if list1 == list(numpy.roll(list2, i)): # shift b circularly by i
            return True
    return False

print(is_dep(list1,list2))