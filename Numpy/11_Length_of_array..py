'''
@Author: Sankar
@Date: 2021-04-14 08:19:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:35:09
@Title : Numpy_Python-11
'''
'''
Write a Python program to find the number of elements of an array, length of one
array element in bytes and total bytes consumed by the elements.
Expected Output:
Size of the array: 3
Length of one array element in bytes: 8
Total bytes consumed by the elements of the array: 24
'''
import numpy as np
arr = np.array([1,2,3], dtype = "float")
print("Size of the array: ",arr.size)
print("Length of one array element in bytes ",arr.itemsize)
print("Total bytes consumed by the elements of the array: ",arr.nbytes)