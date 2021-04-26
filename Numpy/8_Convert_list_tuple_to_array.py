'''
@Author: Sankar
@Date: 2021-04-14 08:19:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:35:09
@Title : Numpy_Python-8
'''
'''
Write a Python program to convert a list and tuple into arrays.
List to array:
[1 2 3 4 5 6 7 8]
Tuple to array:
[[8 4 6]
[1 2 3]]
'''
import numpy as np
list = [1,2,3,4,5,6,7,8]
tuple = ((8,4,6),(1,2,3))
print(np.asarray(list))
print(np.asarray(tuple))