'''
@Author: Sankar
@Date: 2021-04-09 10:22:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 10:30:09
@Title : Dictionary_Python-12
'''
'''
Write a Python program to check multiple keys exists in a dictionary.
'''
dict = {1:1, 2:2, 3:3, 4:4}
if {1,2} <= dict.keys():
    print("True")
else:
    print("False")