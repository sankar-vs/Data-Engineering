'''
@Author: Sankar
@Date: 2021-04-11 12:30:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-11 12:37:09
@Title : Strings_Python-3
'''
'''
Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''
string = "restart"
char = string[0]
string = string.replace(char, "$")
string = char + string[1:]

print(string)