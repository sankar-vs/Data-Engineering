'''
@Author: Sankar
@Date: 2021-04-14 08:02:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:02:09
@Title : Numpy_Python-5
'''
'''
Write a Python program to add a border (filled with 0's) around an existing array.
Expected Output:
Original array:

[[ 1. 1. 1.]
[ 1. 1. 1.]
[ 1. 1. 1.]]
1 on the border and 0 inside in the array
[[ 0. 0. 0. 0. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 0. 0. 0. 0.]]
'''
import numpy as np
arr = np.ones((3,3))
print(arr)
arr = np.pad(arr, pad_width = 1, mode = 'constant', constant_values = 0)
print(arr)