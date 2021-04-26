  
'''
@Author: Sankar
@Date: 2021-04-15 11:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-15 11:10:09
@Title : Pandas_Python-1
'''
'''
Write a Python program to create and display a one-dimensional array-like object
containing an array of data using Pandas module.
'''
import pandas as pd 
import numpy as np 
arr =np.array([1,2,3,4,5,6,7])
series = pd.Series(arr)
print(arr)
print(series)