'''
@Author: Sankar
@Date: 2021-04-09 07:41:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 07:45:09
@Title : Array_Python-3
'''
'''
Write a Python program to get the number of occurrences of a specified element in an array.
'''
array = []
for i in range(5):
    element = int(input("Enter Element {} in array: ".format(i)))
    array.append(element)

print("Count of {} in array {} is: {}".format(3, array, array.count(3)))