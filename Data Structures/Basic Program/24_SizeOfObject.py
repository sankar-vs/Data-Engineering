'''
@Author: Sankar
@Date: 2021-04-08 13:18:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 13:25:09
@Title : Basic_Python-24
'''
'''
Write a Python program to get the size of an object in bytes.
'''
import sys
string = "Get Size"
integer = 50
list = [1, "Hi"]
tuple = (1, "Hello")
float = 111.659
print("Memory Size of {}: {}bytes".format(string, sys.getsizeof(string)))
print("Memory Size of {}: {}bytes".format(integer, sys.getsizeof(integer)))
print("Memory Size of {}: {}bytes".format(list, sys.getsizeof(list)))
print("Memory Size of {}: {}bytes".format(tuple, sys.getsizeof(tuple)))
print("Memory Size of {}: {}bytes".format(float, sys.getsizeof(float)))