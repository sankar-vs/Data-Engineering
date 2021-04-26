'''
@Author: Sankar
@Date: 2021-04-10 07:05:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-10 07:10:09
@Title : List_Python-11
'''
'''
Write a Python program to generate all permutations of a list in Python.
'''
from itertools import permutations

perm = permutations([1,2,3])
for i in list(perm):
    print(i)