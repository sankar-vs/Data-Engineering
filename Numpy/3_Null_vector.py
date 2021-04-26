'''
@Author: Sankar
@Date: 2021-04-13 19:30:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-13 19:39:09
@Title : Numpy_Python-3
'''
'''
Write a Python program to create a null vector of size 10 and update sixth value to 11.
[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
'''
import numpy as np
arr = np.zeros(10)
print(arr)
arr[5] = 11
print(arr)