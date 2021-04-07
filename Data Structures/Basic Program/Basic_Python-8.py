'''
@Author: Sankar
@Date: 2021-04-07 19:55:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 20:12:09
@Title : Basic_Python-8
'''
'''
Write a Python program to create a histogram from a given list of integers.
'''
listInteger = input("Enter integers Comma seperated: ")
list = listInteger.split(",")
for i in list:
    count = int(i)
    output = '*'
    while(count>0):
        output += '*'
        count -= 1
    print(output)
        
