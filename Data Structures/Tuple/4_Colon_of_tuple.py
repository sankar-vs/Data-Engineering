'''
@Author: Sankar
@Date: 2021-04-11 09:18:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-11 09:22:09
@Title : Tuple_Python-4
'''
'''
Write a Python program to create the colon of a tuple.
'''
from copy import deepcopy
tuple =('ya', [], 5, True)
tuple_copy = deepcopy(tuple)
tuple_copy[1].append(7)

print(tuple_copy)