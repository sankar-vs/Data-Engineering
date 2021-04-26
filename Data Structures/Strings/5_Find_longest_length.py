'''
@Author: Sankar
@Date: 2021-04-11 12:47:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-11 12:55:09
@Title : Strings_Python-5
'''
'''
Write a Python function that takes a list of words and returns the length of the longest
one.
'''
list = ["Sam", "Jenny", "Dharmaraj", "Ashish"]
length = len(list[0])
string = list[0]
for i in list:
    if length < len(i):
        length = len(i)
        string = i

print(string, length)