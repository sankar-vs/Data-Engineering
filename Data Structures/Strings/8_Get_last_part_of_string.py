'''
@Author: Sankar
@Date: 2021-04-12 07:49:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-12 07:55:09
@Title : Strings_Python-8
'''
'''
Write a Python program to get the last part of a string before a specified character.
'''
x = 'http://test.com/lalala-134'
print (x.rsplit('-', 1)[0])
print (x.rpartition('-')[0])