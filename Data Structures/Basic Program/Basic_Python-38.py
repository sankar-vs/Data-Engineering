'''
@Author: Sankar
@Date: 2021-04-08 14:39:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 14:45:09
@Title : Basic_Python-38
'''
'''
Write a Python program to add leading zeroes to a string.
'''
String = '151.1987'
print("Add leading zeroes to {} : {}".format(String, String.rjust(12,'0')))
print("Add trailing zeroes to {} : {}".format(String, String.ljust(12,'0')))