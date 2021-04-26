'''
@Author: Sankar
@Date: 2021-04-14 14:34:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 14:45:09
@Title : Numpy_Python-24
'''
'''
Write a Python program to convert a NumPy array into Python list structure.
Expected Output:
Original array elements:
[ 0.26153123 0.52760141 0.5718299 0.5927067 0.7831874 0.69746349
0.35399976 0.99469633 0.0694458 0.54711478]
Print array values with precision 3:
[ 0.262 0.528 0.572 0.593 0.783 0.697 0.354 0.995 0.069 0.547]
'''
import numpy as np
arr = np.array([ 0.26153123,0.52760141,0.5718299,0.5927067,0.7831874,0.69746349,0.35399976,0.99469633,0.0694458,0.54711478])
print(arr)
print(list(np.around(arr, decimals=3)))