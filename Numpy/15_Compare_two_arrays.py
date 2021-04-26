'''
@Author: Sankar
@Date: 2021-04-14 08:49:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:55:09
@Title : Numpy_Python-15
'''
'''
Write a Python program compare two arrays using numpy.
Array a: [1 2]
Array b: [4 5]
a > b
[False False]
a >= b
[False False]
a < b
[ True True]
a <= b
[ True True]
'''
import numpy as np
arr1 = np.array([1, 2])
arr2 = np.array([4, 5])

print("arr1 > arr2: ",np.greater(arr1,arr2))
print("arr1 >= arr2: ",np.greater_equal(arr1,arr2))
print("arr1 < arr2: ",np.less(arr1,arr2))
print("arr1 <= arr2: ",np.less_equal(arr1,arr2))