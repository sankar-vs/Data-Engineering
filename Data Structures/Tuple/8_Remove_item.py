'''
@Author: Sankar
@Date: 2021-04-11 09:33:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-11 09:36:09
@Title : Tuple_Python-8
'''
'''
Write a Python program to remove an item from a tuple.
'''
tuple = ("Heyya", False, 3.2, 1)
print(tuple)
tuple = tuple[:1] + tuple[2:]
print(tuple)