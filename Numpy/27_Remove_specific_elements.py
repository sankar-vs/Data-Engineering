'''
@Author: Sankar
@Date: 2021-04-15 11:00:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-15 11:05:09
@Title : Numpy_Python-27
'''
'''
Write a Python program to remove specific elements in a numpy array.
Expected Output:
Original array:
[ 10 20 30 40 50 60 70 80 90 100]
Delete first, fourth and fifth elements:
[ 20 30 60 70 80 90 100]
'''
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,100])
index = [0,3,4]
arr = np.delete(arr, index)
print(arr)