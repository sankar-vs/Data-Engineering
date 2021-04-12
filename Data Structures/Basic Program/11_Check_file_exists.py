'''
@Author: Sankar
@Date: 2021-04-07 21:52:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 21:58:09
@Title : Basic_Python-11
'''
'''
Write a Python program to check whether a file exists.
'''
import os
if os.path.isfile("Data Structures/Basic Program/Basic_Python-1.py"):
    print("The file exists")
else:
    print("The file does not exists")
