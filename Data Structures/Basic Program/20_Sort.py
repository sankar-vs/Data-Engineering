'''
@Author: Sankar
@Date: 2021-04-08 08:01:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 08:15:09
@Title : Basic_Python-20
'''
'''
Write a Python program to sort three integers without using conditional statements and
loops.
'''
a = int(input("Enter First Integer: "))
b = int(input("Enter Second Integer: "))
c = int(input("Enter Third Integer: "))
max = max(a,b,c)
min = min(a,b,c)
mid = (a+b+c) - min - max
print("Sorted: {} {} {}".format(min, mid, max))