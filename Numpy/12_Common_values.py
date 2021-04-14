'''
@Author: Sankar
@Date: 2021-04-14 08:19:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:35:09
@Title : Numpy_Python-12
'''
'''
Write a Python program to find common values between two arrays.
Expected Output:
Array1: [ 0 10 20 40 60]
Array2: [10, 30, 40]
Common values between two arrays:
[10 40]
'''
import numpy as np
arr1 = np.array([0,10,20,40,60])
arr2 = np.array([10,30,40])

print(np.intersect1d(arr1, arr2))