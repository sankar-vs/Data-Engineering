'''
@Author: Sankar
@Date: 2021-04-08 15:10:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 15:10:09
@Title : Basic_Python-40
'''
'''
Write a Python program to extract single key-value pair of a dictionary in variables.
'''
dict  = {'key1':1,'key2':"value2",3:4}
key = []
value = []
key, value = dict.keys(), dict.values()
print("Keys in the dictinary {} are: {}".format(dict, key))
print("Values in the dictinary {} are: {}".format(dict, value))
print("Specific key in the dictinary {} are: {}".format(dict, {key: dict[key] for key in ['key1'] if key in dict.keys()}))