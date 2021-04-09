'''
@Author: Sankar
@Date: 2021-04-08 15:39:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 15:45:09
@Title : Array_Python-1
'''
'''
Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
'''
array = []
for i in range(5):
    element = int(input("Enter Element {} in array: ".format(i)))
    array.append(element)

print("Element {} of the array is: {}".format(0, array[0]))
print("Element {} of the array is: {}".format(1, array[1]))
print("Element {} of the array is: {}".format(2, array[2]))
print("Element {} of the array is: {}".format(3, array[3]))
print("Element {} of the array is: {}".format(4, array[4]))