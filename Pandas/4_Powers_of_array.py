'''
@Author: Sankar
@Date: 2021-04-15 11:16:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-15 11:21:09
@Title : Pandas_Python-4
'''
'''
Write a Python program to get the powers of an array values element-wise.
Note: First array elements raised to powers from second array
Expected Output:
Original array
[0 1 2 3 4 5 6]
First array elements raised to powers from second array, element-wise:
[ 0 1 8 27 64 125 216]
'''
import numpy as np
arr = np.arange(7)
print(arr)
print(np.power(arr,3))