'''
@Author: Sankar
@Date: 2021-04-15 09:40:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-15 09:45:09
@Title : Numpy_Python-26
'''
'''
Write a Python program to how to add an extra column to an numpy array.
Expected Output:
[[ 10 20 30 100]
[ 40 50 60 200]]
'''
import numpy as np
arr = np.array([[10,20,30],[40,50,60]])
a = np.array([[100],[200]])
arr = np.append(arr,a,axis=1)
print(arr)