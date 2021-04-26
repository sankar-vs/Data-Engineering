'''
@Author: Sankar
@Date: 2021-04-15 08:45:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-15 08:50:09
@Title : Numpy_Python-25
'''
'''
Write a Python program to suppresses the use of scientific notation for small
numbers in numpy array.
Expected Output:
Original array elements:
[ 1.60000000e-10 1.60000000e+00 1.20000000e+03 2.35000000e-01]
Print array values with precision 3:
[ 0. 1.6 1200. 0.235]
'''
import numpy as np
arr = np.array([1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01])
np.set_printoptions(suppress=True)
print(arr)