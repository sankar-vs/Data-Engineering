'''
@Author: Sankar
@Date: 2021-04-14 08:49:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:55:09
@Title : Numpy_Python-14
'''
'''
Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or
will return the sorted, unique values that are in only one (not both) of the input arrays.
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70]
Unique values that are in only one (not both) of the input arrays:
[ 0 20 30 50 60 70 80]
'''
import numpy as np
arr1 = np.array([0, 10, 20, 40, 60, 80])
arr2 = np.array([10, 30, 40, 50, 70])

print(np.setxor1d(arr1, arr2))