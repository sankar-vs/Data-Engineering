'''
@Author: Sankar
@Date: 2021-04-09 07:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 07:51:09
@Title : Array_Python-4
'''
'''
Write a Python program to remove the first occurrence of a specified element from an
array.
'''
array = []
for i in range(5):
    element = int(input("Enter Element {} in array: ".format(i)))
    array.append(element)

arrayResult = array

print("Remove first occurance of {} in array {} is: {}".format(3, array, arrayResult.remove(3)))