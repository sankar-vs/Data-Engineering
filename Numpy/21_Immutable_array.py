'''
@Author: Sankar
@Date: 2021-04-14 13:24:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 13:32:09
@Title : Numpy_Python-21
'''
'''
Write a Python program to make an array immutable (read-only).
Expected Output:
Test the array is read-only or not:
Try to change the value of the first element:
Traceback (most recent call last):
File "19236bd0-0bd9-11e7-a232-c706d0968eb6.py", line 6, in
x[0] = 1
ValueError: assignment destination is read-only
'''
import numpy as np
arr = np.array([1,2,3])
arr.flags.writeable = False
arr[0] = 1