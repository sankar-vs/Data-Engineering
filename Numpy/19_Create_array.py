'''
@Author: Sankar
@Date: 2021-04-14 12:28:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 12:28:09
@Title : Numpy_Python-19
'''
'''
Write a Python program to create an array which looks like below array.
Expected Output:
[[ 0. 0. 0.]
[ 1. 0. 0.]
[ 1. 1. 0.]
[ 1. 1. 1.]]
'''
import numpy as np
arr = np.zeros(12).reshape(4,3)
for i in (1,2,3):
    for j in range(i):
        arr[i][j] = 1
print(arr)