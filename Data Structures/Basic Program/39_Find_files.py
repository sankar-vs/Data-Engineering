'''
@Author: Sankar
@Date: 2021-04-08 14:45:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 15:10:09
@Title : Basic_Python-39
'''
'''
Write a Python program to find files and skip directories of a given directory.
'''
import os
myDirectory = "E:/Practice/Data_Engineering/Data Structures/Basic Program"
list = [f for f in os.listdir(myDirectory) if os.path.isfile(os.path.join(myDirectory, f))]
print(list)