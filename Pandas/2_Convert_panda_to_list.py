'''
@Author: Sankar
@Date: 2021-04-15 11:10:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-15 11:15:09
@Title : Pandas_Python-2
'''
'''
Write a Python program to convert a Panda module Series to Python list and it's type.
'''
import pandas as pd 
s =pd.Series([1,2,3,4,5,6,7])
print(type(s), s)
print(s.tolist(), type(s.tolist()))