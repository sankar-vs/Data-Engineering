'''
@Author: Sankar
@Date: 2021-04-14 12:43:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 12:48:09
@Title : Numpy_Python-20
'''
'''
Write a Python program to concatenate two 2-dimensional arrays.
Expected Output:
Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]])
Expected Output:
[[ 0 1 3 0 2 4]
[ 5 7 9 6 8 10]]
'''
import numpy as np
arr1 = np.array([[0, 1, 3], [5, 7, 9]])
arr2 = np.array([[0, 2, 4], [6, 8, 10]])
print(arr1, arr2)
concArr = np.concatenate((arr1,arr2),1)
print(concArr)