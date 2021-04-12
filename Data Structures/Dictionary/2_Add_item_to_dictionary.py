'''
@Author: Sankar
@Date: 2021-04-09 08:36:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 08:40:09
@Title : Dictionary_Python-2
'''
'''
Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''
dict = {0:10, 1:20}
print("Dict before updating: {}".format(dict))
add = {2:30}
dict.update(add)
print("Dict after updating: {}".format(dict))