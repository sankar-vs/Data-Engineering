'''
@Author: Sankar
@Date: 2021-04-14 08:10:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:15:09
@Title : Numpy_Python-7
'''
'''
Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
Checkerboard pattern:
[[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]]
'''
import numpy as np
arr = np.zeros((8,8), dtype = int)
print(arr)
arr[1::2, ::2] = 1
arr[::2, 1::2] = 1
print(arr)
