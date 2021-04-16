'''
@Author: Sankar
@Date: 2021-04-16 07:49:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 07:55:09
@Title : Matplotlib_Python-2
'''
'''
Write a Python program to draw a line using given axis values with suitable label in the x axis
, y axis and a title
'''
from matplotlib import pyplot as plt
x = [1,2,3,4,5]
y = [2,8,5,6,4]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph')
plt.show()