'''
@Author: Sankar
@Date: 2021-04-08 14:19:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 14:25:09
@Title : Basic_Python-34
'''
'''
Write a Python program to retrieve file properties.
'''
import os
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))