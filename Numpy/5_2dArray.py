'''
@Author: Sankar
@Date: 2021-04-14 08:02:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:02:09
@Title : Numpy_Python-5
'''
'''
Write a Python program to create a 2d array with 1 on the border and 0 inside.
Expected Output:
Original array:
[[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]]
1 on the border and 0 inside in the array
[[ 1. 1. 1. 1. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 1. 1. 1. 1.]]
'''
import numpy as np
arr = np.ones(25).reshape(5,5)
print(arr)
arr[1:-1, 1:-1] = 0
print(arr)