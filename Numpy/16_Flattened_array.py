'''
@Author: Sankar
@Date: 2021-04-14 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 09:12:09
@Title : Numpy_Python-16
'''
'''
Write a Python program to create a contiguous flattened array.
Original array:
[[10 20 30]
[20 40 50]]
New flattened array:
[10 20 30 20 40 50]
'''
import numpy as np
arr = np.array([[10, 20, 30],[20,40,50]])
print(arr)
print(np.ravel(arr))

