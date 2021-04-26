'''
@Author: Sankar
@Date: 2021-04-07 21:40:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 21:44:09
@Title : Basic_Python-9
'''
'''
Write a Python program to concatenate all elements in a list into a string and return it.
'''

list = ['Hi','Sam','Is','Your','Age',53]
print(str(" ".join(map(str, list))))