'''
@Author: Sankar
@Date: 2021-04-13 19:22:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-13 19:35:09
@Title : Numpy_Python-2
'''
'''
Create a 3x3 matrix with values ranging from 2 to 10.
Expected Output:
[[ 2 3 4]
[ 5 6 7]
[ 8 9 10]]
'''
import numpy as np
arr = np.arange(2,11).reshape(3,3)
print(arr)