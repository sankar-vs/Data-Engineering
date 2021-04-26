'''
@Author: Sankar
@Date: 2021-04-15 11:13:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-15 11:17:09
@Title : Pandas_Python-3
'''
'''
Write a Python program to add, subtract, multiple and divide two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
'''
import pandas as pd 
s1 =pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])
print("Add: \n", s1 + s2)
print("Subtract: \n", s1 - s2)
print("Multiply: \n", s1 * s2)
print("Divide: \n", s1 / s2)