'''
@Author: Sankar
@Date: 2021-04-08 15:27:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 15:30:09
@Title : Basic_Python-42
'''
'''
Write a Python program to determine if the python shell is executing in 32bit or 64bit mode
on operating system.
'''
import struct
print("The python shell is execution in {}bit mode".format(8 * struct.calcsize("P")))