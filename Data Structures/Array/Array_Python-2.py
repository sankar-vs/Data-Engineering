'''
@Author: Sankar
@Date: 2021-04-09 07:36:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 07:40:09
@Title : Array_Python-2
'''
'''
Write a Python program to reverse the order of the items in the array.
'''
array = []
for i in range(5):
    element = int(input("Enter Element {} in array: ".format(i)))
    array.append(element)

print("Reverse of array {} is {}".format(array, array[::-1]))