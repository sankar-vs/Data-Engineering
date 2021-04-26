'''
@Author: Sankar
@Date: 2021-04-14 13:24:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 13:32:09
@Title : Numpy_Python-22
'''
'''
Write a Python program to create an array of (3, 4) shape, multiply every element
value by 3 and display the new array.
Expected Output:
Original array elements:
[[ 0 1 2 3]
[ 4 5 6 7]
[ 8 9 10 11]]
New array elements:
[[ 0 3 6 9]
[12 15 18 21]
[24 27 30 33]]
'''
import numpy as np
arr = np.arange(0,12).reshape(3,4)
print(arr)
arr2 = np.array([i*3 for i in arr])
print(arr2)