'''
@Author: Sankar
@Date: 2021-04-13 16:19:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-13 16:35:09
@Title : Numpy_Python-1
'''
'''
Write a Python program to convert a list of numeric value into a one-dimensional
NumPy array.
Expected Output:
Original List: [12.23, 13.32, 100, 36.32]
One-dimensional numpy array: [ 12.23 13.32 100. 36.32]
'''
import numpy as np
list = [12.23, 13.32, 100, 36.32]
arr = np.array(list)
print(arr)