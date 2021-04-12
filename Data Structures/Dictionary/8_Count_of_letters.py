'''
@Author: Sankar
@Date: 2021-04-09 09:57:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 10:01:09
@Title : Dictionary_Python-8
'''
'''
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''
string = "w3resource"
dict = {}
for i in string:
    dict.update({i : string.count(i)})

print("Dictionary: {}".format(dict))