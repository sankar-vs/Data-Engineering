'''
@Author: Sankar
@Date: 2021-04-14 08:19:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:35:09
@Title : Numpy_Python-9
'''
'''
Write a Python program to append values to the end of an array.
Expected Output:
Original array:
[10, 20, 30]
After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]
'''
import numpy as np
arr = np.array([10,20,30])
arr = np.append(arr, [40,50,60,70,80,90])
print(arr)