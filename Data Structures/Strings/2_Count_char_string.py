'''
@Author: Sankar
@Date: 2021-04-11 12:26:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-11 12:35:09
@Title : Strings_Python-2
'''
'''
Write a Python program to count the number of characters (character frequency) in a
string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
string = "google.com"
dict = {}
for i in string:
    dict[i] = string.count(i)

print(dict)