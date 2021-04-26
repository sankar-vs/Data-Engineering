'''
@Author: Sankar
@Date: 2021-04-14 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 09:12:09
@Title : Numpy_Python-17
'''
'''
Write a Python program to change the data type of an array.
Expected Output:
[[ 2 4 6]
[ 6 8 10]]
Data type of the array x is: int32
New Type: float64
[[ 2. 4. 6.]
[ 6. 8. 10.]]
'''
import numpy as np
arr = np.array([[2,4,6],[6,8,10]])
print(arr)
print(arr.dtype)
arr2 = arr.astype(float)
print(arr2)
print(arr2.dtype)

