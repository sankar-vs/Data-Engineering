'''
@Author: Sankar
@Date: 2021-04-09 09:00:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 09:05:09
@Title : Dictionary_Python-4
'''
'''
Write a Python program to iterate over dictionaries using for loops.
'''
dict  = {"key1":1,"key2":"hey","key3":51.26}
for key, value in dict.items():
    print("key {} : values {}".format(key, value))