'''
@Author: Sankar
@Date: 2021-04-14 08:19:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:35:09
@Title : Numpy_Python-10
'''
'''
Write a Python program to find the real and imaginary parts of an array of complex
numbers.
Expected Output:
Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
Real part of the array:
[ 1. 0.70710678]
Imaginary part of the array:
[ 0. 0.70710678]
'''
import numpy as np
arr = np.array([ 1.00000000+0.j, 0.70710678+0.70710678j])
print(arr)
print(arr.real)
print(arr.imag)