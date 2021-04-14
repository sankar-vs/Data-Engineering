'''
@Author: Sankar
@Date: 2021-04-14 08:55:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-14 08:59:09
@Title : Numpy_Python-15
'''
'''
Write a Python program to save a NumPy array to a text file.
'''
import numpy as np
arr = np.array([1, 2, 3])
print(arr)

file = open("Numpy/resources/file.txt", "w+")

content = str(arr)
file.write(content)
file.close()

file = open("Numpy/resources/file.txt", "r")
content = file.read()
  
print("\nContent in file.txt:\n", content)
file.close()

np.savetxt("Numpy/resources/file1.txt", arr)

content = np.loadtxt('Numpy/resources/file1.txt')
print("\nContent in file1.txt:\n", content)