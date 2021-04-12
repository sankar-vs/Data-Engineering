'''
@Author: Sankar
@Date: 2021-04-09 10:01:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 10:08:09
@Title : Dictionary_Python-9
'''
'''
Write a Python program to print a dictionary in table format.
'''
import pandas as pd
dict = {"key1":1,"key2":2,"key3":"Hello","key4":"4"}
df = pd.DataFrame(dict.items(), columns=["keys", "values"])
print(df)