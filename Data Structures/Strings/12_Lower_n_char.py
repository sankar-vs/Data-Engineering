'''
@Author: Sankar
@Date: 2021-04-12 07:55:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-12 07:59:09
@Title : Strings_Python-12
'''
'''
Write a Python program to lowercase first n characters in a string.
'''
str1 = "HEYYA! HOW ARE YOU?"
str2 = str1[:4].lower() + str1[4:]
print(str2)