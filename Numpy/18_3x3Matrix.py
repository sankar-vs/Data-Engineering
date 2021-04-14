'''
@Author: Sankar
@Date: 2021-04-14 09:15:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 09:21:09
@Title : Numpy_Python-18
'''
'''
Write a Python program to create a 3-D array with ones on a diagonal and zeros
elsewhere.
Expected Output:
[[ 1. 0. 0.]
[ 0. 1. 0.]
[ 0. 0. 1.]]
'''
import numpy as np
arr = np.eye(3)
print(arr)


