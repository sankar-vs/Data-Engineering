'''
@Author: Sankar
@Date: 2021-04-14 14:22:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 14:32:09
@Title : Numpy_Python-23
'''
'''
Write a Python program to convert a NumPy array into Python list structure.
Expected Output:
Original array elements:
[[0 1]
[2 3]
[4 5]]
Array to list:
[[0, 1], [2, 3], [4, 5]]
'''
import numpy as np
arr = np.array([[0,1],[2,3],[4,5]])
print(arr)
print(list(np.ravel(arr)))