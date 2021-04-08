'''
@Author: Sankar
@Date: 2021-04-08 08:01:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 08:15:09
@Title : Basic_Python-19
'''
'''
Write a Python program to get file creation and modification date/times.
'''
import os, time
print("Last modified: %s" % time.ctime(os.path.getmtime("Basic_Python-1.py")))
print("Created: %s" % time.ctime(os.path.getctime("Basic_Python-1.py")))